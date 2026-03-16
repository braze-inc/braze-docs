const { execSync } = require('child_process');

const branch = process.env.VERCEL_GIT_COMMIT_REF || '';
const vercel_env = process.env.VERCEL_ENV || 'preview';
const vercel_lang = process.env.LANGUAGE || 'en';

const LANG_DIR_MAP = {
	'de': '_lang/de/',
	'es': '_lang/es/',
	'fr': '_lang/fr_fr/',
	'ja': '_lang/ja/',
	'ko': '_lang/ko/',
	'pt-br': '_lang/pt_br/',
};

const SHARED_DIRS = ['_layouts/', '_plugins/', '_includes/'];

function isTranslationBranch(name) {
	return name.startsWith('i18n_') || name.startsWith('auto-translate/');
}

function getChangedFiles() {
	execSync('git fetch origin develop --depth=1', { stdio: 'ignore' });
	return execSync('git diff --name-only origin/develop...HEAD', { encoding: 'utf-8' })
		.trim().split('\n').filter(Boolean);
}

if (vercel_env === 'production') {
	process.exit(1);
}

if (vercel_lang === 'en') {
	if (isTranslationBranch(branch)) {
		process.exit(0);
	}
	process.exit(1);
}

try {
	const files = getChangedFiles();
	const langDir = LANG_DIR_MAP[vercel_lang];
	const hasLangChanges = langDir && files.some(f => f.startsWith(langDir));
	const hasSharedChanges = files.some(f =>
		SHARED_DIRS.some(d => f.startsWith(d))
	);

	if (hasLangChanges || hasSharedChanges) {
		console.log(`Changes detected for ${vercel_lang} — building`);
		process.exit(1);
	}
	console.log(`No changes for ${vercel_lang} — skipping`);
	process.exit(0);
} catch (e) {
	console.log('Git diff failed, falling back to branch check:', e.message);
	if (isTranslationBranch(branch)) {
		process.exit(1);
	}
	process.exit(0);
}
