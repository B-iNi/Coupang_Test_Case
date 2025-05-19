import { test, expect } from '@playwright/test';
import * as dotenv from 'dotenv';
import path from 'path';


// ────────────실행에 앞서────────────
// npm install dotenv
// npx playwright install
// npm init -y
// npm install -D @playwright/test

// 실행: npx playwright test --ui
// ──────────────────────────────────

dotenv.config({ path: path.resolve(__dirname, '../src/config/.env') });

const EMAIL = process.env.EMAIL!;
const PASSWORD = process.env.PASSWORD!;

// ─────────────────────── 유틸 함수 ───────────────────────
function generateRandomString(length = 8) {
  const chars = 'abcdefghijklmnopqrstuvwxyz0123456789';
  return Array.from({ length }, () => chars[Math.floor(Math.random() * chars.length)]).join('');
}

function generateRandomEmail() {
  return `${generateRandomString(5)}@${generateRandomString(4)}.com`;
}

function generateSpecialUsername() {
  const base = generateRandomString(5);
  const special = '~!@#$%^&*()_+';
  return base + special[Math.floor(Math.random() * special.length)];
}

// ─────────────────────── 로그인 테스트 ───────────────────────
test('로그인 성공 시나리오', async ({ page }) => {
  await page.goto('http://localhost:4100/login');
  if (process.env.DEBUG === 'true') await page.pause();

  await page.fill('input[placeholder="Email"]', EMAIL);
  await page.fill('input[placeholder="Password"]', PASSWORD);
  await page.getByRole('button', { name: 'Sign in' }).click();

  await expect(page).toHaveURL('http://localhost:4100/');
});

// ─────────────────────── 회원가입 테스트 묶음 ───────────────────────
test.describe('회원가입 시나리오 테스트', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('http://localhost:4100/register');
  });

  test('회원가입 UI 요소 및 내비게이션 확인', async ({ page }) => {
    // 입력 필드
    await expect(page.getByPlaceholder('Username')).toBeVisible();
    await expect(page.getByPlaceholder('Email')).toBeVisible();
    await expect(page.getByPlaceholder('Password')).toBeVisible();

    // 네비게이션 요소
    await expect(page.getByRole('button', { name: 'Sign up' })).toBeVisible();
    await expect(page.getByRole('link', { name: 'Have an account?' })).toBeVisible();
    await expect(page.getByRole('link', { name: 'Sign in' })).toBeVisible();
    await expect(page.locator('a.navbar-brand')).toBeVisible();
    await expect(page.getByRole('link', { name: 'Home' })).toBeVisible();
    await expect(page.getByRole('link', { name: 'Sign up' })).toBeVisible();

    // 하단 링크 클릭 → 로그인 페이지 이동
    await page.getByRole('link', { name: 'Have an account?' }).click();
    await expect(page).toHaveURL('http://localhost:4100/login');
  });

  test('입력값 유효성 검사', async ({ page }) => {
    const url = 'http://localhost:4100/register';

    // Username 미입력
    await page.fill('input[placeholder="Email"]', generateRandomEmail());
    await page.fill('input[placeholder="Password"]', generateRandomString());
    await page.getByRole('button', { name: 'Sign up' }).click();
    await expect(page).toHaveURL(url);

    await page.goto(url);

    // Email 미입력
    await page.fill('input[placeholder="Username"]', generateRandomString());
    await page.fill('input[placeholder="Password"]', generateRandomString());
    await page.getByRole('button', { name: 'Sign up' }).click();
    await expect(page).toHaveURL(url);

    await page.goto(url);

    // Email 형식 오류
    await page.fill('input[placeholder="Username"]', generateRandomString());
    await page.fill('input[placeholder="Email"]', generateRandomString()); // 이메일 형식 X
    await page.fill('input[placeholder="Password"]', generateRandomString());
    await page.getByRole('button', { name: 'Sign up' }).click();
    await expect(page).toHaveURL(url);

    await page.goto(url);

    // Password 미입력
    await page.fill('input[placeholder="Username"]', generateRandomString());
    await page.fill('input[placeholder="Email"]', generateRandomEmail());
    await page.getByRole('button', { name: 'Sign up' }).click();
    await expect(page).toHaveURL(url);

    await page.goto(url);

    // 전부 미입력
    await page.getByRole('button', { name: 'Sign up' }).click();
    await expect(page).toHaveURL(url);

    await page.goto(url);

    // 특수문자 포함 Username
    await page.fill('input[placeholder="Username"]', generateSpecialUsername());
    await page.fill('input[placeholder="Email"]', generateRandomEmail());
    await page.fill('input[placeholder="Password"]', generateRandomString());
    await page.getByRole('button', { name: 'Sign up' }).click();
    await expect(page).toHaveURL(url);
  });

  test('회원가입 성공 시 메인페이지로 이동', async ({ page }) => {
    await page.fill('input[placeholder="Username"]', generateRandomString());
    await page.fill('input[placeholder="Email"]', generateRandomEmail());
    await page.fill('input[placeholder="Password"]', generateRandomString());

    await page.getByRole('button', { name: 'Sign up' }).click();
    await expect(page).toHaveURL('http://localhost:4100/');
  });

  test('회원가입 후 프로필 페이지 접근 및 확인', async ({ page }) => {
    const username = generateRandomString();
    const email = generateRandomEmail();
    const password = generateRandomString();

  // 회원가입
    await page.goto('http://localhost:4100/register');
    await page.fill('input[placeholder="Username"]', username);
    await page.fill('input[placeholder="Email"]', email);
    await page.fill('input[placeholder="Password"]', password);
    await page.getByRole('button', { name: 'Sign up' }).click();

  // 프로필 링크 클릭
    await page.click(`a.nav-link:has-text("${username}")`);
    await expect(page).toHaveURL(`http://localhost:4100/@${username}`);
    await expect(page.getByRole('heading', { name: username })).toBeVisible();

});
  test('회원가입 후 로그아웃 및 재로그인 테스트', async ({ page }) => {
    const username = generateRandomString();
    const email = generateRandomEmail();
    const password = generateRandomString();

  // 회원가입
    await page.goto('http://localhost:4100/register');
    await page.fill('input[placeholder="Username"]', username);
    await page.fill('input[placeholder="Email"]', email);
    await page.fill('input[placeholder="Password"]', password);
    await page.getByRole('button', { name: 'Sign up' }).click();

  // 로그아웃
    await page.click('a.nav-link:has-text("Settings")');
    await page.click('button:has-text("Or click here to logout.")');
    await expect(page.getByRole('link', { name: 'Sign in' })).toBeVisible();

  // 로그인
    await page.click('a.nav-link:has-text("Sign in")');
    await page.fill('input[placeholder="Email"]', email);
    await page.fill('input[placeholder="Password"]', password);
    await page.getByRole('button', { name: 'Sign in' }).click();
    await expect(page.getByRole('link', { name: username })).toBeVisible();
});
  test('회원가입 후 설정 페이지 접근 및 사용자 정보 수정 테스트', async ({ page }) => {
    const username = generateRandomString();
    const email = generateRandomEmail();
    const password = generateRandomString();
    const newBio = "이것은 자동화 테스트로 수정된 소개입니다.";
  
    // 회원가입
    await page.goto('http://localhost:4100/register');
    await page.fill('input[placeholder="Username"]', username);
    await page.fill('input[placeholder="Email"]', email);
    await page.fill('input[placeholder="Password"]', password);
    await page.getByRole('button', { name: 'Sign up' }).click();
  
    // 설정 페이지 접근
    await page.click('a.nav-link:has-text("Settings")');
    await expect(page).toHaveURL('http://localhost:4100/settings');
  
    // 사용자 정보 수정
    await page.fill('textarea[placeholder="Short bio about you"]', newBio);
    await page.getByRole('button', { name: 'Update Settings' }).click();
  
    // 메인 페이지로 이동했는지 확인
    await expect(page).toHaveURL('http://localhost:4100/');
  
    // 다시 설정 페이지 접근 후 수정된 소개 확인
    await page.click('a.nav-link:has-text("Settings")');
    await expect(page.locator('textarea[placeholder="Short bio about you"]')).toHaveValue(newBio);
});

});
