import unittest
import os
from app import app, DATA_FILE

class FlaskTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

        # backup data
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                self.original = f.read()
        else:
            self.original = ""

        # clear file
        with open(DATA_FILE, "w") as f:
            f.write("")

    def tearDown(self):
        # restore
        with open(DATA_FILE, "w") as f:
            f.write(self.original)

    # ✅ HOME
    def test_home(self):
        res = self.app.get('/')
        self.assertEqual(res.status_code, 200)

    # ✅ ADD
    def test_add(self):
        res = self.app.post('/', data={
            "title": "Test",
            "description": "Desc"
        }, follow_redirects=True)

        self.assertEqual(res.status_code, 200)

        with open(DATA_FILE) as f:
            self.assertIn("Test|Desc", f.read())

    # ✅ EDIT
    def test_edit(self):
        with open(DATA_FILE, "w") as f:
            f.write("Old|Data\n")

        res = self.app.post('/edit/0', data={
            "title": "New",
            "description": "Updated"
        }, follow_redirects=True)

        self.assertEqual(res.status_code, 200)

        with open(DATA_FILE) as f:
            self.assertIn("New|Updated", f.read())

    # ✅ DELETE
    def test_delete(self):
        with open(DATA_FILE, "w") as f:
            f.write("Delete|Me\n")

        res = self.app.post('/delete/0', follow_redirects=True)

        self.assertEqual(res.status_code, 200)

        with open(DATA_FILE) as f:
            self.assertNotIn("Delete|Me", f.read())


if __name__ == "__main__":
    unittest.main()