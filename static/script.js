let player;
function onYouTubeIframeAPIReady() {
  player = new YT.Player("player", {
    height: "315",
    width: "560",
    videoId: "SpfO55NPhx8",
    events: {
      onStateChange: onPlayerStateChange,
      onReady: onPlayerReady,
    },
  });
}
function onPlayerReady() {
  const progressBar = document.getElementById("progress-bar");
  const completionStatus = document.getElementById("completion-status");
  progressBar.style.width = "0%";
  completionStatus.textContent = "0% Complete";
}
function onPlayerStateChange(event) {
  if (event.data === YT.PlayerState.ENDED) {
    const progressBar = document.getElementById("progress-bar");
    const completionStatus = document.getElementById("completion-status");
    const completionSection = document.getElementById("completion-section");
    progressBar.style.width = "100%";
    completionStatus.textContent = "100% Complete";
    completionSection.style.display = "block";
  }
}
