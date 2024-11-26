from cardloto import Cardloto
import numpy as np

class TestCardloto():
    def setup_method(self):
        self.loto = Cardloto()

    def teardown(self):
        pass

    def test_init(self):
        assert self.loto.close is False
        assert self.loto.name == 'My card'
        assert self.loto.card.shape == (3, 9)

    def test_generate_numbers(self):
        count = self.loto._generate_numbers(1, 1, 3)
        assert len(count)==3

    def test_generate(self):
        self.loto._generate()
        assert np.sum(self.loto.card) > 100

    def test_count_zone(self):
        assert  self.loto._get_count_zone(3, 2) == 3

    def test_check_keg(self):
        assert self.loto.check_keg(-5) is False

    def test_card(self):
        assert self.loto.card.shape == (3, 9)

    def test_del_keg(self):
        assert self.loto.del_keg == []

    def test_close(self):
        assert self.loto.close is False

