import unittest
from app import create_app, db
from app.models import User

class UserModelTestCase(unittest.TestCase):
	def setUp(self):
		self.app = create_app('testing')
		self.app_ctx = self.app.app_context()
		self.app_ctx.push()
		db.create_all()

	def tearDown(self):
		db.drop_all()
		self.app_ctx.pop()

	def test_password(self):
		u = User(username='niraj')
		u.set_password('niraj')
		self.assertTrue(u.verify_password('niraj'))
		self.assertFalse(u.verify_password('pankaj'))

	def test_registration(self):
		User.register('niraj', 'niraj')
		u = User.query.filter_by(username='niraj').first()
		self.assertIsNotNone(u)
		self.assertTrue(u.verify_password('niraj'))
		self.assertFalse(u.verify_password('pankaj'))