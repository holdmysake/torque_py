module.exports = {
    apps: [
        {
            name: "torque-py", // ganti sesuai nama project
            script: "uvicorn",
            args: "main:app --host 0.0.0.0 --port 1111 --reload",
            interpreter: "python3", // interpreter global
            watch: false,
            env: {
                PYTHONUNBUFFERED: "1"
            }
        }
    ]
}