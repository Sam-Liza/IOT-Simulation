class Network(object):

	def __init__(self, download, upload):
		self.download = download
		self.upload = upload

	def timeForDownload(size):
		return size / self.download

	def timeForUpload(size):
		return size / self.upload

class TuftsSecure(Network):
	def __init__(self):
		super(TuftsSecure, self).__init__(190.3, 3.16)

networks = {
	"tufts" : TuftsSecure()
}