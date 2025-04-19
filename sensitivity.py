import copy
from city import City
from strategy import Strategy
import matplotlib.pyplot as plt

class Sensitivity():
    def __init__(self, strategy: Strategy, properties: list[str]):
        self.strategy  = strategy
        self.properties = properties

    def get_variations_array(self, base_value, num_variations, percentage):
        values = []
        for i in range(int(-num_variations/2), int(num_variations/2)):
            variation = base_value + i * percentage * base_value
            values.append(variation)

        return values

    def get_strategies_array(self, variations, property):
        strategies = []
        for variation in variations:
            city = copy.deepcopy(self.strategy.city)
            setattr(city, f"override_{property}", True)
            setattr(city, property, variation)
            strategy = copy.deepcopy(self.strategy)
            strategy.city = city
            strategies.append(strategy)

        return strategies

    def plot_sensitivity(self, property):
        base_value = getattr(self.strategy.city, property)
        variations = self.get_variations_array(base_value, 10, 0.10)
        strategies = self.get_strategies_array(variations, property)
        costs = [strategy.calculate_cost() for strategy in strategies]
        plt.plot(variations, costs, label=property)

    def plot_sensitivities(self):
        for property in self.properties:
            self.plot_sensitivity(property)

        plt.ticklabel_format(useOffset=False)
        plt.ylabel('10-year cost (tens of millions)')
        plt.title('Sensitivity Analysis')
        plt.legend()
        plt.grid(True)
        plt.show()

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

    strategy = Strategy(
        city=city,
        training=True,
        inhouse=True,
        it_services=False,
        insurance=False,
        backups=False,
        pay_ransom=True)

    # sensitivity = Sensitivity(strategy=strategy, properties=["cost_leak", "cost_downtime_bs"])

    sensitivity = Sensitivity(strategy=strategy, properties=["prob_breach", "prob_leak"])

    sensitivity.plot_sensitivities()