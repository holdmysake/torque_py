module.exports = {
    apps: [
        {
            name: "torque-py",
            script: "/_workdir_sawir/torque_py/venv/bin/uvicorn",
            args: "main:app --host 0.0.0.0 --port 1111",
            watch: false,
            env: {
                PYTHONUNBUFFERED: "1"
            }
        }
    ]
}