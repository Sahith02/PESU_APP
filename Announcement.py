from key_generator.key_generator import generate

class Announcement:
	def __init__(self, Title = "", Location = "", Description = "", PictureLink = "", HyperLinks = [], PostingTime = None, ID = None):
		self.ID = generate(num_of_atom = 1, min_atom_len = 10, max_atom_len = 10).get_key() if (ID == None) else ID
		self.Title = Title
		self.Location = Location
		self.Description = Description
		self.PictureLink = PictureLink
		self.HyperLinks = HyperLinks
		self.PostingTime = PostingTime
	
	def ViewAnnouncements(self):
		pass

	def __repr__(self):
		return "\nANNOUNCEMENT:\nID = {0} \nTitle = {1} \nLocation = {2} \nDescription = {3} \nPictureLink = {4} \nHyperLinks = {5} \nPostingTime = {6}\n".format(self.ID, self.Title, self.Location, self.Description, self.PictureLink, self.HyperLinks, self.PostingTime)

A1 = Announcement()
print(A1)