const journal = document.querySelector("#journal");
let stikyScroll = true;
journal.scrollTop = journal.scrollTopMax;

journal.addEventListener("scroll", () => {
  if (stikyScroll && journal.scrollTop != journal.scrollTopMax) {
    stikyScroll = false;
  } else if (!stikyScroll && journal.scrollTop == journal.scrollTopMax) {
    stikyScroll = true;
  }
});

async function fetchJournal() {
  const response = await fetch(document.URL, {headers: {"Accept": "text/stream"}});
  const reader = response.body.getReader();
  const decoder = new TextDecoder("utf-8");

  journal.innerHTML = "";

  while (true) {
    chunk = await reader.read();
    if (chunk.done) {
      break;
    }
    journal.appendChild(document.createTextNode(decoder.decode(chunk.value, {stream: true})));
    if (stikyScroll) {
      journal.scrollTop = journal.scrollTopMax;
      stikyScroll = true;
    }
  }
}

window.onload = fetchJournal;
