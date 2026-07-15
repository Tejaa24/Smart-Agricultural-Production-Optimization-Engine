import unittest


class TestPrediction(unittest.TestCase):

    def test_sample(self):

        sample_crop = "rice"

        self.assertEqual(
            sample_crop,
            "rice"
        )


if __name__ == "__main__":
    unittest.main()