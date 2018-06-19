import eel

web_options = {
	"mode": "chrome-app",
	"host": "localhost",
	"port": 8000,
}
eel.init('web')
eel.start('settings.html', size=(1216, 739), options=web_options)

# Can they get around my restrictions by going to localhost:8000/settings.html?
