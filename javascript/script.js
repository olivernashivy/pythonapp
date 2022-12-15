//custom videoplayer
var video = document.getElementById("video");
var playButton = document.getElementById("play-pause");
var muteButton = document.getElementById("mute");
var fullScreenButton = document.getElementById("full-screen");
var seekBar = document.getElementById("seek-bar");
var volumeBar = document.getElementById("volume-bar");
var currentTime = document.getElementById("current-time");
var duration = document.getElementById("duration");

// Event listener for the play/pause button

playButton.addEventListener("click", function() {
    if (video.paused == true) {
        // Play the video

        video.play();

        // Update the button text to 'Pause'
        
        playButton.innerHTML = "Pause";
    } else {
        // Pause the video
    
        video.pause();
        
        // Update the button text to 'Play'

        playButton.innerHTML = "Play";

    }
});
// hide the control on video start