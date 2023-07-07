import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'

export function middleware(request: NextRequest) {
	let isSpider:boolean = !!request.headers['user-agent'].match(/spider/i);

  if (isSpider) {
		return NextResponse.rewrite(new URL('/blank.html', request.url))
  }

}