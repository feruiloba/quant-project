
from city import City

class Strategy():

    def __init__(
        self,
        city: City,
        training: bool,
        inhouse: bool,
        it_services: bool,
        insurance: bool,
        backups: bool,
        pay_ransom:bool):

        # Initializing attributes
        self.city = city
        self.training = training
        self.inhouse = inhouse
        self.it_services = it_services
        self.insurance = insurance
        self.backups = backups
        self.pay_ransom = pay_ransom

        if self.inhouse and self.it_services:
            raise Exception("inhouse and it_services cannot both be true")

        if self.inhouse and not self.training and not self.insurance:
            raise Exception("inhouse requires training")

    def get_attack_cost(self):
        return self.city.get_prob_attack() * self.get_breach_cost()

    def get_breach_cost(self):
        return self.city.get_prob_breach() * self.get_backup_cost()

    def get_backup_cost(self):
        if self.backups:
            return self.city.get_prob_successful_backup() * self.get_ransom_cost()
        else:
            return self.get_leak_cost() + self.get_no_leak_cost()

    def get_ransom_cost(self):
        if self.pay_ransom:
            return self.city.get_cost_ransom_payment() + self.get_key_cost()
        else:
            return self.get_leak_cost() + self.get_no_leak_cost()

    def get_key_cost(self):
        return self.city.get_prob_key() * (self.get_leak_cost() + self.get_no_leak_cost())

    def get_leak_cost(self):
        leak_cost = self.city.get_prob_leak() * (self.city.get_cost_leak() + self.get_downtime_cost())
        if self.it_services:
            return self.city.get_prob_it_services_leak() * leak_cost
        else:
            return leak_cost

    def get_no_leak_cost(self):
        return (1 - self.city.get_prob_leak()) * (self.get_downtime_cost())

    def get_downtime_cost(self):
        return self.city.get_cost_downtime() + self.get_downtime_bs_cost()

    def get_downtime_bs_cost(self):
        return self.city.get_prob_bs() * self.city.get_cost_downtime_bs()

    def get_services_cost(self):
        cost = 0
        if self.training:
            cost += self.city.get_training_cost()

        if self.inhouse:
            cost += self.city.get_inhouse_cost()

        if self.it_services:
            cost += self.city.get_it_services_cost()

        if self.insurance:
            cost += self.city.get_insurance_cost()

        if self.backups:
            cost += self.city.get_backups_cost()

        return cost

    def calculate_cost(self):
        print(f"Calculating cost for strategy. backups: {self.backups}, pay_ransom: {self.pay_ransom}, training: {self.training}, inhouse: {self.inhouse}, it_services: {self.it_services}, insurance: {self.insurance}")
        return self.get_attack_cost() + self.get_services_cost()


if __name__ == "__main__":

    city = City(
        name="Springfield",
        num_employees=1280,
        num_citizens=500000,
        budget=10000000,
        discount_rate=0.07,
        num_years=10,
        training=True,
        num_sysadmins=10,
        inhouse_cost=1000,
        it_services_cost=1000,
        insurance_cost=1000,
        backups_cost=26214,
        no_backups_cost=1000,
        prob_attack=1,
        prob_key=0.5,
        prob_leak=0.5,
        prob_backup=0.5,
        prob_bs=0.05,
        cost_downtime=100000,
        cost_downtime_bs=10000000,
        cost_data_loss_no_recovery=1000,
        cost_data_loss_recovery=1000,
        cost_leak=100000,
        cost_ransom_key=1000,
        cost_ransom_no_key=1000)

    strategies = [
        Strategy(
            city=city,
            training=False,
            inhouse=False,
            it_services=False,
            insurance=False,
            backups=False,
            pay_ransom=True),
        Strategy(
            city=city,
            training=True,
            inhouse=False,
            it_services=False,
            insurance=False,
            backups=False,
            pay_ransom=True),
    ]

    print("Finding optimal strategy")
    for strategy in strategies:
        print(strategy.calculate_cost())
