module.exports = {
    apps: [
        {
            name: "torque-py",
            script: "uvicorn",
            interpreter: "/_workdir_sawir/torque_py/venv/bin/python",
            args: "main:app --host 127.0.0.1 --port 1317",
            watch: false,
            env: {
                PYTHONUNBUFFERED: "1"
            }
        }
    ]
}