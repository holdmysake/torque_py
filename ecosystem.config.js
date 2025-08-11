module.exports = {
    apps: [
        {
            name: "torque-py",
            script: "uvicorn",
            args: "main:app --host 0.0.0.0 --port 1111",
            interpreter: "/_workdir_sawir/torque_py/venv/bin/python",
            watch: false,
            env: {
                PYTHONUNBUFFERED: "1"
            }
        }
    ]
}