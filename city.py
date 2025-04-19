import numpy as np
import numpy_financial as npf

def expected_value_from_cdf(values, probabilities):
    expected_value = 0
    prev_cdf = 0
    for i in range(len(values)):
        expected_value += values[i] * (probabilities[i] - prev_cdf)
        prev_cdf = probabilities[i]

    return expected_value

class City:
    def __init__(
            self,
            name: str,
            num_employees: int,
            num_citizens: int,
            num_years: int,
            discount_rate: float,
            budget: float,
            training: bool,
            inhouse_cost: float,
            num_sysadmins: int,
            it_services_cost: float,
            insurance_cost: float,
            backups_cost: float,
            no_backups_cost: float,
            prob_attack: float,
            prob_key: float,
            prob_bs: float,
            cost_downtime: float,
            cost_downtime_bs: float,
            cost_leak: float,
            cost_data_loss_recovery: float,
            cost_data_loss_no_recovery: float,
            cost_ransom_key: float,
            cost_ransom_no_key: float,
            override_prob_breach = False,
            prob_breach: float = 0.05,
            override_prob_leak = False,
            prob_leak: float = 0.05,
            override_prob_backup = False,
            prob_backup: float = 0.05,
            ):

        self.name = name
        self.num_employees = num_employees
        self.num_citizens = num_citizens
        self.budget = budget
        self.training = training
        self.num_years = num_years
        self.discount_rate = discount_rate
        self.num_sysadmins = num_sysadmins

        # probabilities
        self.prob_attack = prob_attack
        self.override_prob_key = False
        self.prob_key = prob_key
        self.override_prob_leak = override_prob_leak
        self.prob_leak = prob_leak
        self.override_prob_backup = override_prob_backup
        self.prob_backup = prob_backup
        self.prob_bs = prob_bs
        self.override_prob_breach = override_prob_breach
        self.prob_breach = prob_breach

        # costs
        self.cost_downtime = cost_downtime
        self.cost_downtime_bs = cost_downtime_bs
        self.cost_leak = cost_leak
        self.cost_data_loss_recovery = cost_data_loss_recovery
        self.cost_data_loss_no_recovery = cost_data_loss_no_recovery
        self.cost_ransom_key = cost_ransom_key
        self.cost_ransom_no_key = cost_ransom_no_key
        self.insurance_cost = insurance_cost
        self.it_services_cost = it_services_cost
        self.backups_cost = backups_cost
        self.no_backups_cost = no_backups_cost
        self.inhouse_cost = inhouse_cost

    def __str__(self):
        return (f"City: {self.name}, Employees: {self.num_employees}, "
                f"Citizens: {self.num_citizens}, Budget: ${self.budget:,.2f}")

    def get_prob_attack(self):
        return self.prob_attack

    def get_prob_breach(self):
        if self.override_prob_breach:
            return self.prob_breach

        if self.training:
            return np.average([0.015, 0.03, 0.015, 0.1, 0.03, 0.04 ])
        else:
            return np.average([0.007, 0.005, 0.007, 0.02, 0.002, 0.002])

    def get_cost_ransom_payment(self):
        values = [0, 25000, 50000, 100000, 250000, 500000, 1000000, 10000000, 50000000]
        probabilities = [0, 0.02, 0.1, 0.2, 0.3, 0.5, 0.8, 0.95, 1]

        return expected_value_from_cdf(values, probabilities)

    def get_prob_key(self):
        if self.override_prob_key:
            return self.prob_key

        probabilities = [0.95, 0.90, 0.85, 0.20, 0.98, 0.90]
        return np.average(probabilities)

    def get_prob_successful_backup(self):
        if self.override_prob_backup:
            return self.prob_backup

        probabilities = [0.4, 0.4, 0.3, 0.01, 0.2, 0.3 ]
        return np.average(probabilities)

    def get_prob_leak(self):
        if self.override_prob_leak:
            return self.prob_leak

        probabilities = [0.5, 0.5, 0.3, 0.9, 0.5, 0.4]
        return np.average(probabilities)

    def get_prob_it_services_leak(self):
        return 0.1

    def get_cost_leak(self):
        return self.cost_leak

    def get_cost_downtime(self):
        return self.cost_downtime

    def get_prob_bs(self):
        return self.prob_bs

    def get_cost_downtime_bs(self):
        return self.cost_downtime_bs

    def get_training_cost(self):
        annual_costs = np.full(self.num_years, 5000 + (self.num_employees - 1200) * 5)
        return npf.npv(self.discount_rate, annual_costs)

    def get_inhouse_cost(self):
        salary_fixed_cost_employees = 874450

        salary_sysadmins = self.num_sysadmins * 95360

        annual_costs = np.full(self.num_years, salary_sysadmins + salary_fixed_cost_employees)
        salaries_npv = npf.npv(self.discount_rate, annual_costs)

        recruitment_costs = 4700 * (self.num_sysadmins + 5)

        return recruitment_costs + salaries_npv

    def get_it_services_cost(self):
        return 0

    def get_insurance_cost(self):
        return 0

    def get_backups_cost(self):
        return npf.npv(self.discount_rate, np.full(self.num_years, self.backups_cost))

    def get_no_backups_cost(self):
        return 0

    def get_down_time_cost(self):
        return 0
