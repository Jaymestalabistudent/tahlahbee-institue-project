module.exports = {
  launch: {
	headless: true,
  },
  browserContext: 'default',
  preset: 'jest-puppeteer',
  testTimeout: 30000,
};