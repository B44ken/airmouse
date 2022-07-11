fetch('http://192.168.1.5:80')

const startAccel = () => 0

const handleAccel = (event) => {
	input.updateMouse(accel)
	document.querySelector('code').innerHTML = `${input.mouse.x}, ${input.mouse.y}<br>`
	return accel
}

class Input {
	constructor() {
		this.keyboard = {}
		this.mouse = {x: 0, y: 0}
		this.mouseSpeed = 4
	}
	updateMouse(accel) {
		if(accel.x) this.mouse.x += accel.x * this.mouseSpeed
		if(accel.y) this.mouse.y += accel.y * this.mouseSpeed
	}
}

const input = new Input()
const accel = new Accelerometer()
accel.start()
setInterval(handleAccel, 10)
