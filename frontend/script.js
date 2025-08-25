document.getElementById("uploadForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    let fileInput = document.getElementById("videoInput");
    let file = fileInput.files[0];

    if (!file) {
        alert("กรุณาเลือกไฟล์วิดีโอ");
        return;
    }

    let formData = new FormData();
    formData.append("file", file);

    try {
        let response = await fetch("http://127.0.0.1:5000/upload", {
            method: "POST",
            body: formData
        });

        let data = await response.json();
        if (data.error) {
            document.getElementById("result").innerText = data.error;
        } else {
            document.getElementById("result").innerText =
                `ท่าที่ตรวจพบ: ${data.gesture} (ความมั่นใจ: ${(data.confidence*100).toFixed(2)}%)`;
        }
    } catch (err) {
        document.getElementById("result").innerText = "❌ เกิดข้อผิดพลาดในการเชื่อมต่อ backend";
        console.error(err);
    }
});
