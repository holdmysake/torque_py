module.exports = {
    apps: [
        {
            name: "fastapi-app",
            script: "uvicorn",
            args: "main:app --host 0.0.0.0 --port 8000",
            interpreter: "python3",
            watch: false,
            env: {
                PYTHONUNBUFFERED: "1"
            },
            post_update: [
                "pip install --upgrade pip",
                "pip install -r requirements.txt"
            ]
        }
    ]
}