from sevices.base_services import BaseServices


class CatServices(BaseServices):

    domen = 'https://api.thecatapi.com'
    def search(self):
        params = {"limit": "1"}
        res = self.get(f'{domen}/', params)
        return res