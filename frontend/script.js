const videoInput = document.getElementById("videoInput");
const videoPreview = document.getElementById("videoPreview");
const resultBox = document.getElementById("result");

videoInput.addEventListener("change", () => {
    const file = videoInput.files[0];
    if (file) {
        const url = URL.createObjectURL(file);
        videoPreview.src = url;
        videoPreview.style.display = "block";
    }
});

document.getElementById("uploadForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    let file = videoInput.files[0];
    if (!file) {
        alert("กรุณาเลือกไฟล์วิดีโอ");
        return;
    }

    let formData = new FormData();
    formData.append("file", file);

    resultBox.style.display = "block";
    resultBox.innerText = "⏳ กำลังประมวลผล...";

    try {
        let response = await fetch("http://127.0.0.1:5000/upload", {
            method: "POST",
            body: formData
        });

        let data = await response.json();
        if (data.error) {
            resultBox.innerText = "❌ " + data.error;
        } else {
            resultBox.innerText =
                `✅ ท่าที่ตรวจพบ: ${data.gesture}\n📊 ความมั่นใจ: ${(data.confidence*100).toFixed(2)}%`;
        }
    } catch (err) {
        resultBox.innerText = "❌ เกิดข้อผิดพลาดในการเชื่อมต่อ backend";
        console.error(err);
    }
});
