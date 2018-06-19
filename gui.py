import eel

web_options = {
	"mode": "chrome-app",
	"host": "localhost",
	"port": 8000,
}
eel.init('web')
eel.start('settings.html', size=(1216, 739), options=web_options)
