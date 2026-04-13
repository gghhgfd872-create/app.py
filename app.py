<script>
    async function verifyBot() {
        const token = document.getElementById("botToken").value.trim();
        const btn = document.getElementById("verifyBtn");
        const loading = document.getElementById("loading");
        const result = document.getElementById("result");

        if (!token) {
            showResult("الرجاء إدخال التوكن", "error");
            return;
        }

        btn.disabled = true;
        loading.style.display = "block";
        result.style.display = "none";

        try {
            const response = await fetch("/api/verify-bot", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({token})
            });

            const data = await response.json();

            if (data.success) {
                showBotInfo(data.bot, token);
            } else {
                showResult(data.error || "توكن غير صالح", "error");
            }
        } catch (error) {
            showResult("حدث خطأ في الاتصال", "error");
        } finally {
            btn.disabled = false;
            loading.style.display = "none";
        }
    }

    function showBotInfo(bot, token) {
        const result = document.getElementById("result");
        result.className = "result success";
        result.innerHTML = `
            <h3>✅ تم التحقق بنجاح!</h3>
            <div class="bot-info">
                <div class="info-card">
                    <span>اسم البوت:</span>
                    <strong>${bot.name}</strong>
                </div>
                <div class="info-card">
                    <span>معرف البوت:</span>
                    <strong>@${bot.username}</strong>
                </div>
                <div class="info-card">
                    <span>ID:</span>
                    <strong>${bot.id}</strong>
                </div>
            </div>
            <button class="btn" onclick="setupBot( ${token} )" style="margin-top: 20px;">
                إعداد البوت 🚀
            </button>
        `;
        result.style.display = "block";
    }

    function showResult(message, type) {
        const result = document.getElementById("result");
        result.className = `result ${type}`;
        result.textContent = message;
        result.style.display = "block";
    }

    async function setupBot(token) {
        // الانتقال لصفحة الإعداد
        local

