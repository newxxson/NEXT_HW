const audioFiles = {
  a: "./piano/sound/도_.mp3",
  s: "./piano/sound/레.mp3",
  d: "./piano/sound/미.mp3",
  f: "./piano/sound/파.mp3",
  g: "./piano/sound/솔.mp3",
  h: "./piano/sound/라.mp3",
  j: "./piano/sound/시.mp3",
  k: "./piano/sound/도.mp3",
};

// Create an object to store Audio objects for each key
const audioObjects = {};

// Create Audio objects for each key and set their sources
for (const key in audioFiles) {
  audioObjects[key] = new Audio(audioFiles[key]);
}

window.addEventListener("keydown", (e) => {
  console.log("ininin");
  const key = document.getElementById(e.key);

  if (key) {
    key.classList.add("pressed");
    audioObjects[e.key].currentTime = 0; // Rewind the audio to the start
    audioObjects[e.key].play(); // Play the audio
  }
});

window.addEventListener("keyup", (e) => {
  console.log("outoutout");
  const key = document.getElementById(e.key);
  if (key) {
    key.classList.remove("pressed");
    audioObjects[e.key].pause(); // Pause the audio
    audioObjects[e.key].currentTime = 0; // Rewind the audio to the start
  }
});

console.log("start");
