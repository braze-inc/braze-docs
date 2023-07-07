import { rewrite } from '@vercel/edge';

export function middleware(request: Request) {

	let isSpider:boolean = !!request.headers['user-agent'].match(/spider/i);

  if (isSpider) {
    return rewrite(new URL('/blank.html', request.url));
  }

}