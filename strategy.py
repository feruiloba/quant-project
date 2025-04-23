
from city import City
from nodes import ChanceEdge, ChanceNode, DecisionEdge, DecisionNode, TerminalNode

class Strategy():

    def __init__(
        self,
        city: City):

        # Initializing attributes
        self.city = city

    def build_tree(self):
        edge__1791c = DecisionEdge(name='_a212b', payoff=-1814964, id='1f278e39-f63b-fa40-e9be-b36063a80f78')
        edge__66199 = DecisionEdge(name='_6d70d', payoff=self.city.it_services_cost, id='91af5e2d-1a5d-34fc-bf26-544ea3e3e18b')
        edge__8115f = DecisionEdge(name='_33cc3', payoff=0, id='9666e279-1a8d-b8e3-f2dc-2c67de2cbd27')
        node_9bd785f6_e6fc_af5c_3eb9_b79e0d029cd7 = DecisionNode(name='strategy_packages_4260d', id='9bd785f6-e6fc-af5c-3eb9-b79e0d029cd7', edges=[edge__8115f, edge__1791c, edge__66199])

        edge__b45f3 = DecisionEdge(name='_98ad9', payoff=0, id='bd393914-bdbb-7eba-5caa-c89de07f3217')
        edge__0e0d9 = DecisionEdge(name='_5e832', payoff=0, id='326cee72-42da-75eb-d9fa-0251cd02a0b4')
        node_in_house_with_end_user_training_insurance_e8ba2 = DecisionNode(name='in_house_it_security_department_with_end_user_training_insurance_e8ba2', id='e8adc128-108b-ad97-f793-451b491a9f00', edges=[edge__b45f3, edge__0e0d9])
        edge__1791c.result_node = node_in_house_with_end_user_training_insurance_e8ba2

        edge__60f3a = DecisionEdge(name='_0c34b', payoff=0, id='2a270062-25d4-d957-b2cc-5de79d4678fd')
        node_a14c65a3_af43_6cff_aa75_b7a9699bc19a = DecisionNode(name='no_backup_a9aa9', id='a14c65a3-af43-6cff-aa75-b7a9699bc19a', edges=[edge__60f3a])
        edge__b45f3.result_node = node_a14c65a3_af43_6cff_aa75_b7a9699bc19a

        edge_yes_f19f1 = ChanceEdge(name='yes_0f4da', payoff=0, probability=self.city.prob_attack, id='yes_fd112')
        edge_no_6054f = ChanceEdge(name='no_86dcf', payoff=0, probability=(1-self.city.prob_attack), id='no_1268d')
        node_attack_5386a = ChanceNode(name='attack_5a892', id='attack_5386a', edges=[edge_yes_f19f1, edge_no_6054f])
        edge__60f3a.result_node = node_attack_5386a

        edge_paid_b5f8b = DecisionEdge(name='paid_32564', payoff=self.city.cost_ransom_payment, id='6ea6e441-a51e-0dae-0740-8feabce05af6')
        edge_dont_pay_45eb9 = DecisionEdge(name='dont_pay_c4aae', payoff=0, id='2b3a9329-cf34-692b-2b44-6ae0660e4704')
        node_bee5e71b_9527_0989_d816_bf090d203809 = DecisionNode(name='pay_ransom_9af59', id='bee5e71b-9527-0989-d816-bf090d203809', edges=[edge_paid_b5f8b, edge_dont_pay_45eb9])
        edge_yes_f19f1.result_node = node_bee5e71b_9527_0989_d816_bf090d203809

        edge_obtain_key_f3952 = ChanceEdge(name='obtain_key_d572c', payoff=0, probability=self.city.prob_key, id='obtain_key_fc979')
        edge_no_key_ce4ee = ChanceEdge(name='no_key_be221', payoff=self.city.cost_ransom_no_key, probability=(1-self.city.prob_key), id='no_key_eb49d')
        node_key_f52ff = ChanceNode(name='key_9dc90', id='key_f52ff', edges=[edge_obtain_key_f3952, edge_no_key_ce4ee])
        edge_paid_b5f8b.result_node = node_key_f52ff

        edge_leak_e63d5 = ChanceEdge(name='leak_12263', payoff=self.city.cost_leak, probability=self.city.prob_leak, id='leak_b0be3')
        edge_no_leak_f6dee = ChanceEdge(name='no_leak_edd6a', payoff=0, probability=(1-self.city.prob_leak), id='no_leak_eac2c')
        node_data_leak_a9deb = ChanceNode(name='data_leak_19c3e', id='data_leak_a9deb', edges=[edge_leak_e63d5, edge_no_leak_f6dee])
        edge_obtain_key_f3952.result_node = node_data_leak_a9deb

        edge_leak_8093b = ChanceEdge(name='leak_56533', payoff=-3691680, probability=self.city.prob_leak, id='leak_e93e4')
        edge_no_leak_eb3c9 = ChanceEdge(name='no_leak_14286', payoff=0, probability=(1-self.city.prob_leak), id='no_leak_d54f9')
        node_data_leak_54d26 = ChanceNode(name='data_leak_95cbb', id='data_leak_54d26', edges=[edge_leak_8093b, edge_no_leak_eb3c9])
        edge_no_key_ce4ee.result_node = node_data_leak_54d26

        edge_leak_034c7 = ChanceEdge(name='leak_dbece', payoff=self.city.cost_leak, probability=self.city.prob_leak, id='leak_44936')
        edge_no_leak_80643 = ChanceEdge(name='no_leak_6ad7d', payoff=0, probability=(1-self.city.prob_leak), id='no_leak_57b82')
        node_data_leak_6540e = ChanceNode(name='data_leak_0e902', id='data_leak_6540e', edges=[edge_leak_034c7, edge_no_leak_80643])
        edge_dont_pay_45eb9.result_node = node_data_leak_6540e

        edge__23e76 = DecisionEdge(name='_7315f', payoff=0, id='50ca98a4-6a82-0d95-a9af-15555799172e')
        node_01b7cfc2_ca1b_4341_4476_8b9165603fc2 = DecisionNode(name='backup_5fa5c', id='01b7cfc2-ca1b-4341-4476-8b9165603fc2', edges=[edge__23e76])
        edge__0e0d9.result_node = node_01b7cfc2_ca1b_4341_4476_8b9165603fc2

        edge_yes_7910c = ChanceEdge(name='yes_d196d', payoff=0, probability=self.city.prob_attack, id='yes_10897')
        edge_no_788ba = ChanceEdge(name='no_06408', payoff=0, probability=(1-self.city.prob_attack), id='no_4997a')
        node_attack_730f6 = ChanceNode(name='attack_92fc8', id='attack_730f6', edges=[edge_yes_7910c, edge_no_788ba])
        edge__23e76.result_node = node_attack_730f6

        edge_failed_c253b = ChanceEdge(name='failed_ee33f', payoff=0, probability=(1-self.city.prob_backup), id='failed_ff0d4')
        edge__65f92 = ChanceEdge(name='_508e6', payoff=0, probability=self.city.prob_backup, id='_e705f')
        node_backup_good__1320b = ChanceNode(name='backup_good__4e919', id='backup_good__1320b', edges=[edge_failed_c253b, edge__65f92])
        edge_yes_7910c.result_node = node_backup_good__1320b

        edge_paid_a3557 = DecisionEdge(name='paid_2b068', payoff=self.city.cost_ransom_payment, id='17839fa6-99f3-0fd5-bc7f-4f8c02c31753')
        edge_dont_pay_e64ce = DecisionEdge(name='dont_pay_6bb5e', payoff=0, id='f40f784d-fad7-8795-c224-9d5d61de55b2')
        node_7695dd7e_d8c6_f9f3_eb34_00158319b798 = DecisionNode(name='pay_ransom_34f07', id='7695dd7e-d8c6-f9f3-eb34-00158319b798', edges=[edge_paid_a3557, edge_dont_pay_e64ce])
        edge_failed_c253b.result_node = node_7695dd7e_d8c6_f9f3_eb34_00158319b798

        edge_obtain_key_504ce = ChanceEdge(name='obtain_key_df083', payoff=0, probability=self.city.prob_key, id='obtain_key_682b8')
        edge_no_key_2645a = ChanceEdge(name='no_key_10a90', payoff=-self.city.cost_ransom_no_key, probability=(1-self.city.prob_key), id='no_key_2544d')
        node_key_2ff5c = ChanceNode(name='key_76c34', id='key_2ff5c', edges=[edge_obtain_key_504ce, edge_no_key_2645a])
        edge_paid_a3557.result_node = node_key_2ff5c

        edge_leak_268dc = ChanceEdge(name='leak_cb935', payoff=self.city.cost_leak, probability=self.city.prob_leak, id='leak_6f71b')
        edge_no_leak_b6d92 = ChanceEdge(name='no_leak_e0502', payoff=0, probability=(1-self.city.prob_leak), id='no_leak_442cd')
        node_data_leak_a28d0 = ChanceNode(name='data_leak_7da4c', id='data_leak_a28d0', edges=[edge_leak_268dc, edge_no_leak_b6d92])
        edge_obtain_key_504ce.result_node = node_data_leak_a28d0

        edge_leak_b1a2d = ChanceEdge(name='leak_3c622', payoff=-3691680, probability=self.city.prob_leak, id='leak_8bd13')
        edge_no_leak_02f15 = ChanceEdge(name='no_leak_d348f', payoff=0, probability=(1-self.city.prob_leak), id='no_leak_859cf')
        node_data_leak_4826a = ChanceNode(name='data_leak_aad06', id='data_leak_4826a', edges=[edge_leak_b1a2d, edge_no_leak_02f15])
        edge_no_key_2645a.result_node = node_data_leak_4826a

        edge_leak_a304e = ChanceEdge(name='leak_5fac7', payoff=-3691680, probability=self.city.prob_leak, id='leak_5ab72')
        edge_no_leak_a0709 = ChanceEdge(name='no_leak_636cb', payoff=0, probability=(1-self.city.prob_leak), id='no_leak_caee7')
        node_data_leak_32b9a = ChanceNode(name='data_leak_e870f', id='data_leak_32b9a', edges=[edge_leak_a304e, edge_no_leak_a0709])
        edge_dont_pay_e64ce.result_node = node_data_leak_32b9a

        edge_leak_ef2a0 = ChanceEdge(name='leak_10e9f', payoff=self.city.cost_leak, probability=self.city.prob_leak, id='leak_d39b4')
        edge_no_leak_b65e9 = ChanceEdge(name='no_leak_1a35c', payoff=0, probability=(1-self.city.prob_leak), id='no_leak_aa4ae')
        node_data_leak_aa929 = ChanceNode(name='data_leak_da17e', id='data_leak_aa929', edges=[edge_leak_ef2a0, edge_no_leak_b65e9])
        edge__65f92.result_node = node_data_leak_aa929

        edge__5e316 = DecisionEdge(name='_d7694', payoff=0, id='643caf29-f1d2-0c56-854a-5cf639a5bd3e')
        node_external_it_securityinsurance_included_5dac9 = DecisionNode(name='external_it_securityinsurance_included_5dac9', id='d45d94b0-302e-442d-5069-267cc52167ee', edges=[edge__5e316])
        edge__66199.result_node = node_external_it_securityinsurance_included_5dac9

        edge_leak_ea176 = ChanceEdge(name='leak_aaa6f', payoff=self.city.cost_leak, probability=0.1, id='leak_a06ad')
        edge_no_leak_ea79b = ChanceEdge(name='no_leak_7fa81', payoff=0, probability=0.9, id='no_leak_4bb13')
        node_data_leak_4ca7a = ChanceNode(name='data_leak_27a01', id='data_leak_4ca7a', edges=[edge_leak_ea176, edge_no_leak_ea79b])
        edge__5e316.result_node = node_data_leak_4ca7a

        edge__2f351 = DecisionEdge(name='_09370', payoff=0, id='9f667b7a-adc8-9fb4-4dbd-08933976dc56')
        node_5738f723_e394_bab9_f925_2d38e48f1f2c = DecisionNode(name='do_nothing_f80e9', id='5738f723-e394-bab9-f925-2d38e48f1f2c', edges=[edge__2f351])
        edge__8115f.result_node = node_5738f723_e394_bab9_f925_2d38e48f1f2c

        edge_no_f8ecc = ChanceEdge(name='no_f4264', payoff=0, probability=(1-self.city.prob_attack), id='no_6604a')
        edge_yes_67d71 = ChanceEdge(name='yes_20d6b', payoff=0, probability=self.city.prob_attack, id='yes_f864e')
        node_attack_072d1 = ChanceNode(name='attack_05277', id='attack_072d1', edges=[edge_yes_67d71, edge_no_f8ecc])
        edge__2f351.result_node = node_attack_072d1

        edge_paid_62c2e = DecisionEdge(name='paid_76876', payoff=self.city.cost_ransom_payment, id='84b4fb69-d802-2081-4bcc-9d29fe3d4499')
        node_4293311a_0094_2366_c8d9_8c99cbf2bbdc = DecisionNode(name='pay_ransom_7aead', id='4293311a-0094-2366-c8d9-8c99cbf2bbdc', edges=[edge_paid_62c2e])
        edge_yes_67d71.result_node = node_4293311a_0094_2366_c8d9_8c99cbf2bbdc

        edge_obtain_key_1c39e = ChanceEdge(name='obtain_key_95df3', payoff=-(self.city.cost_ransom_payment), probability=self.city.prob_key, id='obtain_key_59152') # negative ransom payment since key was obtained
        edge_no_key_70ebb = ChanceEdge(name='no_key_e40ad', payoff=-self.city.cost_ransom_no_key, probability=(1-self.city.prob_key), id='no_key_e99a1')
        node_key_31dd6 = ChanceNode(name='key_406c7', id='key_31dd6', edges=[edge_obtain_key_1c39e, edge_no_key_70ebb])
        edge_paid_62c2e.result_node = node_key_31dd6

        edge_no_leak_20eae = ChanceEdge(name='no_leak_359e1', payoff=0, probability=(1-self.city.prob_leak), id='no_leak_14d58')
        edge_leak_deb5b = ChanceEdge(name='leak_07f43', payoff=self.city.cost_leak, probability=self.city.prob_leak, id='leak_b8ec1')
        node_data_leak_c732a = ChanceNode(name='data_leak_cc9b9', id='data_leak_c732a', edges=[edge_leak_deb5b, edge_no_leak_20eae])
        edge_obtain_key_1c39e.result_node = node_data_leak_c732a

        edge_no_leak_77cb7 = ChanceEdge(name='no_leak_164ab', payoff=0, probability=(1-self.city.prob_leak), id='no_leak_c26b7')
        edge_leak_62a58 = ChanceEdge(name='leak_be68e', payoff=-3691680, probability=self.city.prob_leak, id='leak_0d3f3')
        node_data_leak_4739b = ChanceNode(name='data_leak_7757c', id='data_leak_4739b', edges=[edge_leak_62a58, edge_no_leak_77cb7])
        edge_no_key_70ebb.result_node = node_data_leak_4739b

        node_de9eeec0_8116_f60f_6f73_2efe98bbe768 = TerminalNode(name='_9e2f5', id='de9eeec0-8116-f60f-6f73-2efe98bbe768')
        edge_leak_ea176.result_node = node_de9eeec0_8116_f60f_6f73_2efe98bbe768

        node_9c03659f_66f6_36f7_3ab7_d53ac2f7d970 = TerminalNode(name='_5e30f', id='9c03659f-66f6-36f7-3ab7-d53ac2f7d970')
        edge_no_leak_ea79b.result_node = node_9c03659f_66f6_36f7_3ab7_d53ac2f7d970

        node_c5b874a6_5b88_2f46_a4cb_98e70f7ee443 = TerminalNode(name='_1e620', id='c5b874a6-5b88-2f46-a4cb-98e70f7ee443')
        edge_no_leak_20eae.result_node = node_c5b874a6_5b88_2f46_a4cb_98e70f7ee443

        node_892f5180_47b6_0e81_8aed_4464a8e3c008 = TerminalNode(name='_6a62e', id='892f5180-47b6-0e81-8aed-4464a8e3c008')
        edge_leak_deb5b.result_node = node_892f5180_47b6_0e81_8aed_4464a8e3c008

        node_4da370b8_e53b_0822_ee30_7f47838c51f5 = TerminalNode(name='_9fdc4', id='4da370b8-e53b-0822-ee30-7f47838c51f5')
        edge_no_leak_77cb7.result_node = node_4da370b8_e53b_0822_ee30_7f47838c51f5

        node_9e3c94db_a639_2da0_905a_ef8ef5443f76 = TerminalNode(name='_ec4ac', id='9e3c94db-a639-2da0-905a-ef8ef5443f76')
        edge_leak_62a58.result_node = node_9e3c94db_a639_2da0_905a_ef8ef5443f76

        node_49f721fc_2b60_1241_fefe_3fde197359ba = TerminalNode(name='_31546', id='49f721fc-2b60-1241-fefe-3fde197359ba')
        edge_no_788ba.result_node = node_49f721fc_2b60_1241_fefe_3fde197359ba

        node_83a180b1_5660_749e_44fc_6b0b30243514 = TerminalNode(name='_18294', id='83a180b1-5660-749e-44fc-6b0b30243514')
        edge_leak_268dc.result_node = node_83a180b1_5660_749e_44fc_6b0b30243514

        node_7aeb7fce_96a0_5325_066d_9ce2ddb09242 = TerminalNode(name='_9cc98', id='7aeb7fce-96a0-5325-066d-9ce2ddb09242')
        edge_no_leak_b6d92.result_node = node_7aeb7fce_96a0_5325_066d_9ce2ddb09242

        node_0b9e74c9_e702_fecc_e9b7_7b5099fc2661 = TerminalNode(name='_8123d', id='0b9e74c9-e702-fecc-e9b7-7b5099fc2661')
        edge_no_f8ecc.result_node = node_0b9e74c9_e702_fecc_e9b7_7b5099fc2661

        node_f2141636_b18c_1d09_5d24_26c7d2333b51 = TerminalNode(name='_e5c6c', id='f2141636-b18c-1d09-5d24-26c7d2333b51')
        edge_leak_ef2a0.result_node = node_f2141636_b18c_1d09_5d24_26c7d2333b51

        node_1c4e04e0_c37e_2eef_6de3_437f4b83142c = TerminalNode(name='_a74d4', id='1c4e04e0-c37e-2eef-6de3-437f4b83142c')
        edge_no_leak_b65e9.result_node = node_1c4e04e0_c37e_2eef_6de3_437f4b83142c

        node_5300516e_cc7e_566c_3e71_956de1229c89 = TerminalNode(name='_c35b2', id='5300516e-cc7e-566c-3e71-956de1229c89')
        edge_leak_a304e.result_node = node_5300516e_cc7e_566c_3e71_956de1229c89

        node_c2009aa5_fcdf_b4f5_a95d_4ef3a1b05756 = TerminalNode(name='_a3f15', id='c2009aa5-fcdf-b4f5-a95d-4ef3a1b05756')
        edge_no_leak_a0709.result_node = node_c2009aa5_fcdf_b4f5_a95d_4ef3a1b05756

        node_08e2510b_0401_63d8_899e_e96f0634f448 = TerminalNode(name='_0fc21', id='08e2510b-0401-63d8-899e-e96f0634f448')
        edge_no_6054f.result_node = node_08e2510b_0401_63d8_899e_e96f0634f448

        node_4eef8a6a_d256_c390_f39f_b15d737729d3 = TerminalNode(name='_75f51', id='4eef8a6a-d256-c390-f39f-b15d737729d3')
        edge_leak_8093b.result_node = node_4eef8a6a_d256_c390_f39f_b15d737729d3

        node_dba2a79e_7241_4660_cbb4_a14f466e5713 = TerminalNode(name='_53e9c', id='dba2a79e-7241-4660-cbb4-a14f466e5713')
        edge_leak_e63d5.result_node = node_dba2a79e_7241_4660_cbb4_a14f466e5713

        node_c7cd1883_d39b_4024_dfa1_9b2f7cfed392 = TerminalNode(name='_05390', id='c7cd1883-d39b-4024-dfa1-9b2f7cfed392')
        edge_no_leak_f6dee.result_node = node_c7cd1883_d39b_4024_dfa1_9b2f7cfed392

        node_ff0e1b89_3e02_d449_2a8b_5b808c67d333 = TerminalNode(name='_b2ea9', id='ff0e1b89-3e02-d449-2a8b-5b808c67d333')
        edge_no_leak_eb3c9.result_node = node_ff0e1b89_3e02_d449_2a8b_5b808c67d333

        node_3a016884_7d74_c60e_e39b_1dcd89a93bf0 = TerminalNode(name='_b97dd', id='3a016884-7d74-c60e-e39b-1dcd89a93bf0')
        edge_leak_034c7.result_node = node_3a016884_7d74_c60e_e39b_1dcd89a93bf0

        node_6bdc5172_1b34_3e78_f115_8260853e35f6 = TerminalNode(name='_52c83', id='6bdc5172-1b34-3e78-f115-8260853e35f6')
        edge_no_leak_80643.result_node = node_6bdc5172_1b34_3e78_f115_8260853e35f6

        node_73edb5a9_7027_a877_bd1d_6352009d47c3 = TerminalNode(name='_c2d67', id='73edb5a9-7027-a877-bd1d-6352009d47c3')
        edge_leak_b1a2d.result_node = node_73edb5a9_7027_a877_bd1d_6352009d47c3

        node_1eee9364_9819_f8b6_cb21_d90e1298867d = TerminalNode(name='_7799b', id='1eee9364-9819-f8b6-cb21-d90e1298867d')
        edge_no_leak_02f15.result_node = node_1eee9364_9819_f8b6_cb21_d90e1298867d

        return node_9bd785f6_e6fc_af5c_3eb9_b79e0d029cd7


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

    strategy = Strategy(city)
    tree = strategy.build_tree()
    tree.print_tree()
    # print(tree.get_payoff())


