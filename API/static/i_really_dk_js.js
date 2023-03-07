async function funk() {

    let ind = parseInt(sessionStorage.getItem("ind")) || 1;

    const ctx = new AudioContext();
    let audio;
    await fetch("/bips", { method: 'GET', headers: { 'index': ind.toString() }, cache: "no-cache"} )
        .then(data => data.arrayBuffer())
        .then(arrayBuffer => ctx.decodeAudioData(arrayBuffer))
        .then(decodedAudio => {
            audio = decodedAudio;
        })

    ind += 1
    sessionStorage.setItem("ind", ind.toString());

    function playback() {
        const playSound = ctx.createBufferSource();
        playSound.buffer = audio;
        playSound.connect(ctx.destination);
        playSound.start(ctx.currentTime);
    }

    playback()

}

async function copyUrl() {
  try {
    await navigator.clipboard.writeText(location.href);
  } catch (err) {
    console.error(err);
  }
  let text = document.getElementById("cptext");
  text.classList.add("fade-in");
  setTimeout(function () {
    text.classList.remove("fade-in");
  }, 1000);
}


document.querySelector("#boop_butt").addEventListener("click", funk)
document.querySelector("#share_butt").addEventListener("click", copyUrl)

