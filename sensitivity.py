import copy
from city import City
from strategy import Strategy
import matplotlib.pyplot as plt
import numpy as np


class Sensitivity():
    def __init__(self, strategy: Strategy, properties: list[str], property_names: list[str]):
        self.strategy = strategy
        self.properties = properties
        self.property_names = property_names

    def get_variations_array(self, base_value, percentages):
        return [base_value + i * base_value for i in percentages]

    def get_strategies_array(self, variations, property):
        strategies = []
        for variation in variations:
            city = copy.deepcopy(self.strategy.city)
            setattr(city, property, variation)
            strategy = copy.deepcopy(self.strategy)
            strategy.city = city
            strategies.append(strategy)

        return strategies

    def plot_sensitivity(self, property, percentages):
        base_value = getattr(self.strategy.city, property)
        variations = self.get_variations_array(base_value, percentages)
        strategies = self.get_strategies_array(variations, property)
        costs = [min(strategy.build_tree().get_payoff(), 0)
                 for strategy in strategies]
        plt.plot(percentages, costs, label=property)

    def plot_sensitivities(self):
        percentages = [i * 0.1 for i in range(-10, 10)]
        for property in self.properties:
            self.plot_sensitivity(property, percentages)

        plt.ticklabel_format(useOffset=False, style='plain')
        plt.xlabel('Change (%)')
        plt.ylabel('Cost')
        plt.title('Sensitivity Analysis')
        plt.legend(self.property_names)
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def tornado_chart(self):
        num_properties = len(self.properties)

        base_value = getattr(self.strategy.city, property)
        variations = self.get_variations_array(base_value, percentages)
        strategies = self.get_strategies_array(variations, property)
        costs = [min(strategy.build_tree().get_payoff(), 0)
                 for strategy in strategies]

        fig, (ax_left, ax_right) = plt.subplots(ncols=num_properties)

        negative_percentages = percentages = [i * 0.1 for i in range(-10, 0)]
        positive_percentages = percentages = [i * 0.1 for i in range(0, 10)]
        for property in self.properties:

            base_value = getattr(self.strategy.city, property)
            x_values_left = self.get_variations_array(
                base_value, negative_percentages)
            strategies_left = self.get_strategies_array(
                x_values_left, property)
            y_values_left = [strategy.build_tree().get_payoff()
                             for strategy in strategies_left]

            x_values_right = self.get_variations_array(
                base_value, positive_percentages)
            strategies_right = self.get_strategies_array(
                x_values_right, property)
            y_values_right = [strategy.build_tree().get_payoff()
                              for strategy in strategies_right]

            ax_left.barh(x_values_left, y_values_left,
                         align="center", facecolor="cornflowerblue")

            ax_left.set_yticks(x_values_left)

            ax_left.set_xlabel("Change (%)")

            ax_left.invert_xaxis()

            ax_right.barh(x_values_right, y_values_right,
                          align="center", facecolor="lemonchiffon")

            ax_right.set_yticks(x_values_right)

        plt.show()


if __name__ == "__main__":
    city = City(
        name="Springfield",
        num_employees=1280,
        num_citizens=500000,
        budget=10000000,
        discount_rate=0.07,
        num_years=10,
        num_sysadmins=10,
        prob_leak=0.5166666666666667,
        prob_key=0.7966666666666666,
        prob_attack=0.03833333333333333,
        prob_backup=0.2683333333333333,
        prob_bs=0,
        cost_ransom_payment=-164243000,
        inhouse_cost=0,
        it_services_cost=-600000,
        insurance_cost=0,
        backups_cost=0,
        no_backups_cost=0,
        cost_downtime=0,
        cost_downtime_bs=0,
        cost_leak=-319168,
        cost_data_loss_recovery=0,
        cost_data_loss_no_recovery=0,
        cost_ransom_key=0,
        cost_ransom_no_key=-66045000)

    strategy = Strategy(city=city)

    sensitivity = Sensitivity(strategy=strategy,
        properties=[
            "prob_attack",
            "prob_leak",
            "prob_key",
            "prob_backup",
            "cost_ransom_payment",
            "it_services_cost",
            "cost_leak",
            "cost_ransom_no_key"
        ],
        property_names=[
            "Probability of attack",
            "Probability of leak",
            "Probability of key",
            "Probability of backup",
            "Ransom payment cost",
            "IT services cost",
            "Leak cost",
            "No key provided cost"
    ])

    sensitivity.plot_sensitivities()

    # sensitivity.tornado_chart()
