// The site moved from aldier-site.pages.dev to aldier.pages.dev.
// Visitors who arrive at the old address are sent to the same page at the new one.
export async function onRequest(context) {
  const url = new URL(context.request.url);
  if (url.hostname === "aldier-site.pages.dev") {
    url.hostname = "aldier.pages.dev";
    return Response.redirect(url.toString(), 301);
  }
  return context.next();
}
