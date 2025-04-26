
from matplotlib import ticker

import copy
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys

sys.path.insert(0, '/home/feruiloba/quant-project/strategies')
from strategy import Strategy, City
from strategy_new import StrategyNew

class Sensitivity():
    def __init__(self, strategy: StrategyNew, properties: list[str], property_names: list[str]):
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

    def plot_sensitivity(self, property, percentages, line_style):
        line_styles = ['-', '--', '-.', ':']
        base_value = getattr(self.strategy.city, property)
        variations = self.get_variations_array(base_value, percentages)
        strategies = self.get_strategies_array(variations, property)
        costs = [min(strategy.build_tree().get_payoff(), 0)
                 for strategy in strategies]
        plt.plot(percentages, costs, label=property)

    def plot_sensitivities(self):
        percentages = [i * 0.1 for i in range(-10, 10)]
        for line_style, property in enumerate(self.properties):
            self.plot_sensitivity(property, percentages, line_style)

        plt.ticklabel_format(useOffset=False, style='plain')
        plt.xlabel('Change (%)')
        plt.ylabel('Expected Yearly Cost of Best Strategy')
        plt.title('Sensitivity Analysis')
        plt.legend(self.property_names)
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    @staticmethod
    def plot_stacked_bar_chart():
        # create data
        df = pd.DataFrame(
            data=[
                ['A', 10, 20, 10, 26],
                ['B', 20, 25, 15, 21],
                ['C', 12, 15, 19, 6],
                ['D', 10, 18, 11, 19]],
            columns=['Team', 'Round 1', 'Round 2', 'Round 3', 'Round 4'])
        df.plot(
            x='Team',
            kind='barh',
            stacked=True,
            title='Stacked Bar Graph by dataframe')

        plt.show()

    @staticmethod
    def plot_bar_chart():
        data = [
                ['External + Insurance + User Training', 842921.6 * 4.16/1000000 ],
                ['User Training', 6884621.15 * 0.736 / 1000000],
                ['In House + User Training + Insurance', 2005383.3 * 4.16/1000000],
                ['Baseline', 6884621.15 * 4.16 / 1000000]]

        # Sample data
        df = pd.DataFrame(data=data, columns=["Expert", "Cost"])

        # Create the bar chart
        df.plot(x='Expert', kind='barh', figsize=(10, 6))

        # Add title and labels
        plt.title('Yearly cost of ransomware attacks')
        plt.xlabel('Cost')
        plt.ylabel('Strategy package')
        plt.xticks(range(0, int(df["Cost"].max()+5), 5))
        plt.rcParams["font.size"] = 22
        plt.ticklabel_format(style='plain', axis='x')

        # Show the plot
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    @staticmethod
    def plot_box_plot():
        # Sample data
        df = pd.DataFrame(
            data=[
                np.random.normal(loc=0, scale=1, size=10),
                np.random.normal(loc=0, scale=1, size=10),
                np.random.normal(loc=0, scale=1, size=10),
                np.random.normal(loc=0, scale=1, size=10)])

        # Create the box plot
        df.plot(kind='box')

        # Add title and labels
        plt.title('Box Plot Example')
        plt.ylabel('Values')

        # Show the plot
        plt.show()

    @staticmethod
    def bar_chart_with_bounds():

        # 1. Data
        categories = ['Expert 1', 'Expert 2', 'Expert 3', 'Expert 5', 'Expert 6', 'Mean']

        ransom = 4439000
        # (min, max) for each
        intervals = [
            (18345 + ransom * 100 * 0.015, 25035 + ransom * 100 * 0.015),
            (162570 + ransom * 100 * 0.03, 162570 + ransom * 100 * 0.03),
            (42300 + ransom * 200 * 0.015, 120900 + ransom * 200 * 0.015),
            (400500 + ransom * 250 * 0.03, 472500 + ransom * 250 * 0.03),
            (70245 + ransom * 150 * 0.04, 70245 + ransom * 150 * 0.04),
            (18345 + ransom * 160 * 0.038, 472500 + ransom * 160 * 0.038)
        ]

        # diamond markers for point estimates (x, idx, color)
        markers = [
            (162570 + ransom * 100 * 0.03,  1, "orange"),
            (70245 + ransom * 150 * 0.04,  4, "orange"),
            (245422.5 + ransom * 160 * 0.038, 5, "blue")
        ]

        # indices of the bars that should be dashed‐outline (e.g. Geothermal, Coal, Nuclear)
        dashed_idx = [5]

        # 2. Plot
        fig, ax = plt.subplots(figsize=(12, 6))
        y = list(range(len(categories)))

        # a) solid bars
        for i, (mn, mx) in enumerate(intervals):
            width = mx - mn
            if i in dashed_idx:
                # dashed outline
                ax.barh(i, width, left=mn,
                        facecolor="none",
                        edgecolor="gray",
                        linestyle="--",
                        height=0.8)
            else:
                ax.barh(i, width, left=mn,
                        color="navy",
                        height=0.8)

        # b) diamond markers
        for x, idx, color in markers:
            ax.scatter(x, idx,
                    marker="D",
                    s=80,
                    color=color,
                    edgecolor="black",
                    zorder=5)

        # c) separator
        sep = 4.5  # between the 4th and 5th item
        ax.axhline(sep, color="black", linewidth=1)

        # d) annotations
        for i, (mn, mx) in enumerate(intervals):
            ax.text(mn-4500, i, f"${mn}", va="center", ha="right") # color="white" if i not in dashed_idx else "gray"
            if i in dashed_idx or i not in [t[1] for t in markers]:
                ax.text(mx+4500, i, f"${mx}", va="center", ha="left")

        # 3. Styling
        ax.set_yticks(y)
        ax.set_yticklabels(categories)
        ax.invert_yaxis()           # so the first item is at the top
        ax.set_xlim(6000000, 38000000)  # set x‐axis limits
        ax.set_xlabel("Total yearly cost (millions)")
        plt.title("Distribution of yearly costs by expert (excluding ransom payment)")
        plt.ticklabel_format(style='plain', axis='x')
        plt.tight_layout()
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
        prob_leak=0.44, # without expert 4
        prob_key=0.916, # without expert 4
        prob_attack=0.03833333333333333,
        prob_backup = 0.32,# without expert 4
        prob_bs=0,
        cost_ransom_payment=-164243000,
        inhouse_cost=0,
        it_services_cost=-600000,
        insurance_cost=0,
        backups_cost=0,
        no_backups_cost=0,
        cost_downtime=0,
        cost_downtime_bs=0,
        cost_leak_key=-319168,
        cost_leak_no_key=-136592160,
        cost_data_loss_recovery=0,
        cost_data_loss_no_recovery=0,
        cost_ransom_key=0,
        cost_ransom_no_key=-66045000)

    strategy = StrategyNew(city=city)

    sensitivity = Sensitivity(
        strategy=strategy,
        properties=[
            "prob_attack",
            # "prob_leak",
            # "prob_key",
            # "prob_backup",
            # "cost_ransom_payment",
            "it_services_cost",
            "cost_leak_key",
            # "cost_ransom_no_key"
        ],
        property_names=[
            "Probability of attack",
            # "Probability of leak",
            # "Probability of key",
            # "Probability of backup",
            # "Ransom payment cost",
            "IT services cost",
            "Leak cost",
            # "No key provided cost"
    ])

    # sensitivity.plot_sensitivities()

    # sensitivity.plot_bar_chart()

    sensitivity.bar_chart_with_bounds()
