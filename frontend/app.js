const input = document.getElementById("imageInput");
const preview = document.getElementById("preview");
const screenBtn = document.getElementById("screenBtn");
const status = document.getElementById("status");

input.addEventListener("change", () => {
  const file = input.files[0];
  if (!file) return;
  preview.src = URL.createObjectURL(file);
  preview.classList.remove("hidden");
  screenBtn.disabled = false;
  status.textContent = file.name;
});

screenBtn.addEventListener("click", async () => {
  const file = input.files[0];
  if (!file) return;

  screenBtn.disabled = true;
  status.textContent = "Processing image...";

  const form = new FormData();
  form.append("image", file);

  try {
    const response = await fetch("http://127.0.0.1:5000/api/screen", {
      method: "POST",
      body: form
    });

    const data = await response.json();
    if (!response.ok) throw new Error(data.error || "Screening failed");

    document.getElementById("severity").textContent = data.severity;
    document.getElementById("risk").textContent = data.risk;
    document.getElementById("confidence").textContent =
      `${Math.round(data.confidence * 100)}%`;
    document.getElementById("confidenceBar").style.width =
      `${Math.round(data.confidence * 100)}%`;
    document.getElementById("explanation").textContent = data.explanation;
    document.getElementById("recommendation").textContent = data.recommendation;
    status.textContent = "Demo screening completed.";
  } catch (error) {
    status.textContent = error.message +
      " Make sure the Flask backend is running.";
  } finally {
    screenBtn.disabled = false;
  }
});
