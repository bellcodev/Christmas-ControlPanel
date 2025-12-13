function startSnow() {
    const canvas = document.getElementById("snowCanvas")
    const ctx = canvas.getContext("2d")

    function resize() {
        canvas.width = window.innerWidth
        canvas.height = window.innerHeight
    }
    resize()
    window.addEventListener("resize", resize)

    const flakes = []
    const totalFlakes = 120

    for (let i = 0; i < totalFlakes; i++) {
        flakes.push({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height,
            r: Math.random() * 3 + 1,
            d: Math.random() + 1
        })
    }

    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height)
        ctx.fillStyle = "white"
        ctx.beginPath()

        for (let f of flakes) {
            ctx.moveTo(f.x, f.y)
            ctx.arc(f.x, f.y, f.r, 0, Math.PI * 2)
        }

        ctx.fill()
        update()
    }

    let angle = 0
    function update() {
        angle += 0.01

        for (let f of flakes) {
            f.y += Math.pow(f.d, 2) + 1
            f.x += Math.sin(angle) * 0.5

            if (f.y > canvas.height) {
                f.y = -10
                f.x = Math.random() * canvas.width
            }
        }
    }

    setInterval(draw, 33)
}

startSnow()
