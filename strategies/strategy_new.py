import sys
sys.path.insert(0, '/home/feruiloba/quant-project/trees')

from city import City
from nodes import ChanceEdge, ChanceNode, DecisionEdge, DecisionNode, TerminalNode
from strategy import Strategy


class StrategyNew(Strategy):

    def __init__(self, city: City):
        super().__init__(city)

    def build_tree(self):
        edge__3e6e0 = DecisionEdge(name='_372d4', payoff=0, id='9666e279-1a8d-b8e3-f2dc-2c67de2cbd27')
        edge__818b4 = DecisionEdge(name='_0e574', payoff=0, id='9f667b7a-adc8-9fb4-4dbd-08933976dc56')
        edge_yes_0cd08 = ChanceEdge(name='yes_cdbae', payoff=0, probability=self.city.prob_attack, id='yes_60f50')
        edge_paid_bea96 = DecisionEdge(name='paid_cfd11', payoff=self.city.cost_ransom_payment, id='84b4fb69-d802-2081-4bcc-9d29fe3d4499')
        edge_obtain_key_55398 = ChanceEdge(name='obtain_key_7de5f', payoff=0, probability=self.city.prob_key, id='obtain_key_4ef51')
        edge_leak_3aa5a = ChanceEdge(name='leak_b23f7', payoff=self.city.cost_leak_key*37, probability=self.city.prob_leak, id='leak_c3a0b')
        node_892f5180_47b6_0e81_8aed_4464a8e3c008 = TerminalNode(name='_a0ad6', id='892f5180-47b6-0e81-8aed-4464a8e3c008')
        edge_no_leak_0f54d = ChanceEdge(name='no_leak_641bd', payoff=0, probability=(1-self.city.prob_leak), id='no_leak_436f7')
        node_c5b874a6_5b88_2f46_a4cb_98e70f7ee443 = TerminalNode(name='_5420b', id='c5b874a6-5b88-2f46-a4cb-98e70f7ee443')
        node_data_leak_b9290 = ChanceNode(name='data_leak_d90ad', id='data_leak_b9290', edges=[edge_leak_3aa5a, edge_no_leak_0f54d])
        edge_no_key_eeabc = ChanceEdge(name='no_key_e54e8', payoff=self.city.cost_ransom_no_key, probability=(1-self.city.prob_key), id='no_key_3eada')
        edge_leak_9136f = ChanceEdge(name='leak_a5d68', payoff=self.city.cost_leak_no_key, probability=self.city.prob_leak, id='leak_9dd38')
        node_9e3c94db_a639_2da0_905a_ef8ef5443f76 = TerminalNode(name='_33f53', id='9e3c94db-a639-2da0-905a-ef8ef5443f76')
        edge_no_leak_39a4c = ChanceEdge(name='no_leak_a5802', payoff=0, probability=(1-self.city.prob_leak), id='no_leak_5aaa2')
        node_4da370b8_e53b_0822_ee30_7f47838c51f5 = TerminalNode(name='_1737b', id='4da370b8-e53b-0822-ee30-7f47838c51f5')
        node_data_leak_280bc = ChanceNode(name='data_leak_fafca', id='data_leak_280bc', edges=[edge_leak_9136f, edge_no_leak_39a4c])
        node_key_fb085 = ChanceNode(name='key_5f001', id='key_fb085', edges=[edge_obtain_key_55398, edge_no_key_eeabc])
        node_4293311a_0094_2366_c8d9_8c99cbf2bbdc = DecisionNode(name='pay_ransom_d0f4e', id='4293311a-0094-2366-c8d9-8c99cbf2bbdc', edges=[edge_paid_bea96])
        edge_no_cfe00 = ChanceEdge(name='no_d05fb', payoff=0, probability=(1-self.city.prob_attack), id='no_aeedf')
        node_0b9e74c9_e702_fecc_e9b7_7b5099fc2661 = TerminalNode(name='_8a8b4', id='0b9e74c9-e702-fecc-e9b7-7b5099fc2661')
        node_attack_8be44 = ChanceNode(name='attack_aa016', id='attack_8be44', edges=[edge_yes_0cd08, edge_no_cfe00])
        node_5738f723_e394_bab9_f925_2d38e48f1f2c = DecisionNode(name='do_nothing_5f74a', id='5738f723-e394-bab9-f925-2d38e48f1f2c', edges=[edge__818b4])
        edge__34fa0 = DecisionEdge(name='_a5bd9', payoff=-2000000, id='1f278e39-f63b-fa40-e9be-b36063a80f78')
        edge__40528 = DecisionEdge(name='_cb8ff', payoff=0, id='bd393914-bdbb-7eba-5caa-c89de07f3217')
        edge__14f6e = DecisionEdge(name='_51f6f', payoff=0, id='2a270062-25d4-d957-b2cc-5de79d4678fd')
        edge_yes_963bc = ChanceEdge(name='yes_3e452', payoff=0, probability=self.city.prob_attack, id='yes_c641c')
        edge_paid_27f2c = DecisionEdge(name='paid_35cac', payoff=self.city.cost_ransom_payment, id='6ea6e441-a51e-0dae-0740-8feabce05af6')
        edge_obtain_key_7b725 = ChanceEdge(name='obtain_key_c5771', payoff=0, probability=self.city.prob_key, id='obtain_key_6ac74')
        edge_leak_2df68 = ChanceEdge(name='leak_54025', payoff=-self.city.cost_leak_key*37+10000000 - 20000*31, probability=self.city.prob_leak, id='leak_02589')
        node_dba2a79e_7241_4660_cbb4_a14f466e5713 = TerminalNode(name='_1a4b5', id='dba2a79e-7241-4660-cbb4-a14f466e5713')
        edge_no_leak_fdd7f = ChanceEdge(name='no_leak_e8be4', payoff=0, probability=(1-self.city.prob_leak), id='no_leak_02c68')
        node_c7cd1883_d39b_4024_dfa1_9b2f7cfed392 = TerminalNode(name='_dbde1', id='c7cd1883-d39b-4024-dfa1-9b2f7cfed392')
        node_data_leak_01295 = ChanceNode(name='data_leak_faefe', id='data_leak_01295', edges=[edge_leak_2df68, edge_no_leak_fdd7f])
        edge_no_key_d28ae = ChanceEdge(name='no_key_31650', payoff=self.city.cost_ransom_no_key+10000000-40000, probability=(1-self.city.prob_key), id='no_key_f9741')
        edge_leak_8e0e9 = ChanceEdge(name='leak_a2e1d', payoff=self.city.cost_leak_no_key, probability=self.city.prob_leak, id='leak_2bda5')
        node_4eef8a6a_d256_c390_f39f_b15d737729d3 = TerminalNode(name='_29eed', id='4eef8a6a-d256-c390-f39f-b15d737729d3')
        edge_no_leak_1da94 = ChanceEdge(name='no_leak_cebec', payoff=0, probability=(1-self.city.prob_leak), id='no_leak_38a67')
        node_ff0e1b89_3e02_d449_2a8b_5b808c67d333 = TerminalNode(name='_6392e', id='ff0e1b89-3e02-d449-2a8b-5b808c67d333')
        node_data_leak_7855d = ChanceNode(name='data_leak_5b939', id='data_leak_7855d', edges=[edge_leak_8e0e9, edge_no_leak_1da94])
        node_key_0cf5f = ChanceNode(name='key_09d64', id='key_0cf5f', edges=[edge_obtain_key_7b725, edge_no_key_d28ae])
        edge_dont_pay_dbf6d = DecisionEdge(name='dont_pay_d2ddd', payoff=0, id='2b3a9329-cf34-692b-2b44-6ae0660e4704')
        edge_leak_bce3e = ChanceEdge(name='leak_0cb4e', payoff=self.city.cost_leak_key, probability=self.city.prob_leak, id='leak_daff6')
        node_3a016884_7d74_c60e_e39b_1dcd89a93bf0 = TerminalNode(name='_26fc1', id='3a016884-7d74-c60e-e39b-1dcd89a93bf0')
        edge_no_leak_d5cee = ChanceEdge(name='no_leak_63029', payoff=0, probability=(1-self.city.prob_leak), id='no_leak_11f1f')
        node_6bdc5172_1b34_3e78_f115_8260853e35f6 = TerminalNode(name='_842da', id='6bdc5172-1b34-3e78-f115-8260853e35f6')
        node_data_leak_e05e3 = ChanceNode(name='data_leak_654c7', id='data_leak_e05e3', edges=[edge_leak_bce3e, edge_no_leak_d5cee])
        node_bee5e71b_9527_0989_d816_bf090d203809 = DecisionNode(name='pay_ransom_9448d', id='bee5e71b-9527-0989-d816-bf090d203809', edges=[edge_paid_27f2c, edge_dont_pay_dbf6d])
        edge_no_6cf22 = ChanceEdge(name='no_db3e5', payoff=0, probability=(1-self.city.prob_attack), id='no_78b95')
        node_08e2510b_0401_63d8_899e_e96f0634f448 = TerminalNode(name='_0119c', id='08e2510b-0401-63d8-899e-e96f0634f448')
        node_attack_13f2c = ChanceNode(name='attack_0ae94', id='attack_13f2c', edges=[edge_yes_963bc, edge_no_6cf22])
        node_a14c65a3_af43_6cff_aa75_b7a9699bc19a = DecisionNode(name='no_backup_98236', id='a14c65a3-af43-6cff-aa75-b7a9699bc19a', edges=[edge__14f6e])
        edge__9247d = DecisionEdge(name='_88e5c', payoff=0, id='326cee72-42da-75eb-d9fa-0251cd02a0b4')
        edge__e09c3 = DecisionEdge(name='_bc07b', payoff=0, id='50ca98a4-6a82-0d95-a9af-15555799172e')
        edge_yes_b9ad0 = ChanceEdge(name='yes_4a344', payoff=0, probability=self.city.prob_attack, id='yes_b136d')
        edge_failed_4a551 = ChanceEdge(name='failed_4c3af', payoff=0, probability=(1-self.city.prob_backup), id='failed_83a22')
        edge_paid_26dea = DecisionEdge(name='paid_023c7', payoff=self.city.cost_ransom_payment, id='17839fa6-99f3-0fd5-bc7f-4f8c02c31753')
        edge_obtain_key_94653 = ChanceEdge(name='obtain_key_a1cf5', payoff=0, probability=self.city.prob_key, id='obtain_key_c12ed')
        edge_leak_8a019 = ChanceEdge(name='leak_2a154', payoff=self.city.cost_leak_key*37+10000000 - 20000*31, probability=self.city.prob_leak, id='leak_5686a')
        node_83a180b1_5660_749e_44fc_6b0b30243514 = TerminalNode(name='_34b91', id='83a180b1-5660-749e-44fc-6b0b30243514')
        edge_no_leak_f826c = ChanceEdge(name='no_leak_e1ef0', payoff=0, probability=(1-self.city.prob_leak), id='no_leak_9b312')
        node_7aeb7fce_96a0_5325_066d_9ce2ddb09242 = TerminalNode(name='_c9780', id='7aeb7fce-96a0-5325-066d-9ce2ddb09242')
        node_data_leak_1c51e = ChanceNode(name='data_leak_2e6b5', id='data_leak_1c51e', edges=[edge_leak_8a019, edge_no_leak_f826c])
        edge_no_key_c6b9e = ChanceEdge(name='no_key_5615a', payoff=self.city.cost_ransom_no_key+10000000-40000, probability=(1-self.city.prob_key), id='no_key_0bd0b')
        edge_leak_05032 = ChanceEdge(name='leak_4c71f', payoff=self.city.cost_leak_no_key, probability=self.city.prob_leak, id='leak_9e9cb')
        node_73edb5a9_7027_a877_bd1d_6352009d47c3 = TerminalNode(name='_9b152', id='73edb5a9-7027-a877-bd1d-6352009d47c3')
        edge_no_leak_62237 = ChanceEdge(name='no_leak_52d35', payoff=0, probability=(1-self.city.prob_leak), id='no_leak_5e4e7')
        node_1eee9364_9819_f8b6_cb21_d90e1298867d = TerminalNode(name='_ab0c3', id='1eee9364-9819-f8b6-cb21-d90e1298867d')
        node_data_leak_15894 = ChanceNode(name='data_leak_de9d5', id='data_leak_15894', edges=[edge_leak_05032, edge_no_leak_62237])
        node_key_39d67 = ChanceNode(name='key_565a9', id='key_39d67', edges=[edge_obtain_key_94653, edge_no_key_c6b9e])
        edge_dont_pay_de811 = DecisionEdge(name='dont_pay_b7b57', payoff=10000000-40000, id='f40f784d-fad7-8795-c224-9d5d61de55b2')
        edge_leak_bf162 = ChanceEdge(name='leak_d3141', payoff=self.city.cost_leak_no_key, probability=self.city.prob_leak, id='leak_a017b')
        node_5300516e_cc7e_566c_3e71_956de1229c89 = TerminalNode(name='_81210', id='5300516e-cc7e-566c-3e71-956de1229c89')
        edge_no_leak_5e7e2 = ChanceEdge(name='no_leak_31e7d', payoff=0, probability=(1-self.city.prob_leak), id='no_leak_b5910')
        node_c2009aa5_fcdf_b4f5_a95d_4ef3a1b05756 = TerminalNode(name='_cf88a', id='c2009aa5-fcdf-b4f5-a95d-4ef3a1b05756')
        node_data_leak_41ba3 = ChanceNode(name='data_leak_8eed6', id='data_leak_41ba3', edges=[edge_leak_bf162, edge_no_leak_5e7e2])
        node_7695dd7e_d8c6_f9f3_eb34_00158319b798 = DecisionNode(name='pay_ransom_fd28f', id='7695dd7e-d8c6-f9f3-eb34-00158319b798', edges=[edge_paid_26dea, edge_dont_pay_de811])
        edge_worked_1e707 = ChanceEdge(name='worked_51b7b', payoff=0, probability=self.city.prob_backup, id='worked_0d011')
        edge_leak_03616 = ChanceEdge(name='leak_1eec3', payoff=self.city.cost_leak_key*37+10000000 - 20000*31, probability=self.city.prob_leak, id='leak_bdcc1')
        node_f2141636_b18c_1d09_5d24_26c7d2333b51 = TerminalNode(name='_15e0e', id='f2141636-b18c-1d09-5d24-26c7d2333b51')
        edge_no_leak_d67f0 = ChanceEdge(name='no_leak_25bf8', payoff=0, probability=(1-self.city.prob_leak), id='no_leak_162c9')
        node_1c4e04e0_c37e_2eef_6de3_437f4b83142c = TerminalNode(name='_23979', id='1c4e04e0-c37e-2eef-6de3-437f4b83142c')
        node_data_leak_52557 = ChanceNode(name='data_leak_6cae2', id='data_leak_52557', edges=[edge_leak_03616, edge_no_leak_d67f0])
        node_backup_good__0e09d = ChanceNode(name='backup_good__32d6b', id='backup_good__0e09d', edges=[edge_failed_4a551, edge_worked_1e707])
        edge_no_17cdb = ChanceEdge(name='no_2c2d7', payoff=0, probability=(1-self.city.prob_attack), id='no_dc95d')
        node_49f721fc_2b60_1241_fefe_3fde197359ba = TerminalNode(name='_d0067', id='49f721fc-2b60-1241-fefe-3fde197359ba')
        node_attack_53cab = ChanceNode(name='attack_6bf05', id='attack_53cab', edges=[edge_yes_b9ad0, edge_no_17cdb])
        node_01b7cfc2_ca1b_4341_4476_8b9165603fc2 = DecisionNode(name='backup_c2a10', id='01b7cfc2-ca1b-4341-4476-8b9165603fc2', edges=[edge__e09c3])
        node_e8adc128_108b_ad97_f793_451b491a9f00 = DecisionNode(name='in_house_it_security_department_with_end_user_training__insurance_d6030', id='e8adc128-108b-ad97-f793-451b491a9f00', edges=[edge__40528, edge__9247d])
        edge__c5c61 = DecisionEdge(name='_25ad2', payoff=self.city.it_services_cost, id='91af5e2d-1a5d-34fc-bf26-544ea3e3e18b')
        edge__045e5 = DecisionEdge(name='_c9b63', payoff=0, id='643caf29-f1d2-0c56-854a-5cf639a5bd3e')
        edge_leak_39160 = ChanceEdge(name='leak_68aaa', payoff=self.city.cost_leak_key*37+10000000 - 20000*31, probability=0.1, id='leak_a820a')
        node_de9eeec0_8116_f60f_6f73_2efe98bbe768 = TerminalNode(name='_3ec96', id='de9eeec0-8116-f60f-6f73-2efe98bbe768')
        edge_no_leak_7c43a = ChanceEdge(name='no_leak_4ac48', payoff=0, probability=0.9, id='no_leak_cb1f3')
        node_9c03659f_66f6_36f7_3ab7_d53ac2f7d970 = TerminalNode(name='_bf5a3', id='9c03659f-66f6-36f7-3ab7-d53ac2f7d970')
        node_data_leak_48217 = ChanceNode(name='data_leak_6bd3b', id='data_leak_48217', edges=[edge_leak_39160, edge_no_leak_7c43a])
        node_d45d94b0_302e_442d_5069_267cc52167ee = DecisionNode(name='external_it_securityinsurance_included_ad807', id='d45d94b0-302e-442d-5069-267cc52167ee', edges=[edge__045e5])
        node_9bd785f6_e6fc_af5c_3eb9_b79e0d029cd7 = DecisionNode(name='strategy_packages_8cc2f', id='9bd785f6-e6fc-af5c-3eb9-b79e0d029cd7', edges=[edge__3e6e0, edge__34fa0, edge__c5c61])
        edge__3e6e0.result_node = node_5738f723_e394_bab9_f925_2d38e48f1f2c
        edge__818b4.result_node = node_attack_8be44
        edge_yes_0cd08.result_node = node_4293311a_0094_2366_c8d9_8c99cbf2bbdc
        edge_paid_bea96.result_node = node_key_fb085
        edge_obtain_key_55398.result_node = node_data_leak_b9290
        edge_leak_3aa5a.result_node = node_892f5180_47b6_0e81_8aed_4464a8e3c008
        edge_no_leak_0f54d.result_node = node_c5b874a6_5b88_2f46_a4cb_98e70f7ee443
        edge_no_key_eeabc.result_node = node_data_leak_280bc
        edge_leak_9136f.result_node = node_9e3c94db_a639_2da0_905a_ef8ef5443f76
        edge_no_leak_39a4c.result_node = node_4da370b8_e53b_0822_ee30_7f47838c51f5
        edge_no_cfe00.result_node = node_0b9e74c9_e702_fecc_e9b7_7b5099fc2661
        edge__34fa0.result_node = node_e8adc128_108b_ad97_f793_451b491a9f00
        edge__40528.result_node = node_a14c65a3_af43_6cff_aa75_b7a9699bc19a
        edge__14f6e.result_node = node_attack_13f2c
        edge_yes_963bc.result_node = node_bee5e71b_9527_0989_d816_bf090d203809
        edge_paid_27f2c.result_node = node_key_0cf5f
        edge_obtain_key_7b725.result_node = node_data_leak_01295
        edge_leak_2df68.result_node = node_dba2a79e_7241_4660_cbb4_a14f466e5713
        edge_no_leak_fdd7f.result_node = node_c7cd1883_d39b_4024_dfa1_9b2f7cfed392
        edge_no_key_d28ae.result_node = node_data_leak_7855d
        edge_leak_8e0e9.result_node = node_4eef8a6a_d256_c390_f39f_b15d737729d3
        edge_no_leak_1da94.result_node = node_ff0e1b89_3e02_d449_2a8b_5b808c67d333
        edge_dont_pay_dbf6d.result_node = node_data_leak_e05e3
        edge_leak_bce3e.result_node = node_3a016884_7d74_c60e_e39b_1dcd89a93bf0
        edge_no_leak_d5cee.result_node = node_6bdc5172_1b34_3e78_f115_8260853e35f6
        edge_no_6cf22.result_node = node_08e2510b_0401_63d8_899e_e96f0634f448
        edge__9247d.result_node = node_01b7cfc2_ca1b_4341_4476_8b9165603fc2
        edge__e09c3.result_node = node_attack_53cab
        edge_yes_b9ad0.result_node = node_backup_good__0e09d
        edge_failed_4a551.result_node = node_7695dd7e_d8c6_f9f3_eb34_00158319b798
        edge_paid_26dea.result_node = node_key_39d67
        edge_obtain_key_94653.result_node = node_data_leak_1c51e
        edge_leak_8a019.result_node = node_83a180b1_5660_749e_44fc_6b0b30243514
        edge_no_leak_f826c.result_node = node_7aeb7fce_96a0_5325_066d_9ce2ddb09242
        edge_no_key_c6b9e.result_node = node_data_leak_15894
        edge_leak_05032.result_node = node_73edb5a9_7027_a877_bd1d_6352009d47c3
        edge_no_leak_62237.result_node = node_1eee9364_9819_f8b6_cb21_d90e1298867d
        edge_dont_pay_de811.result_node = node_data_leak_41ba3
        edge_leak_bf162.result_node = node_5300516e_cc7e_566c_3e71_956de1229c89
        edge_no_leak_5e7e2.result_node = node_c2009aa5_fcdf_b4f5_a95d_4ef3a1b05756
        edge_worked_1e707.result_node = node_data_leak_52557
        edge_leak_03616.result_node = node_f2141636_b18c_1d09_5d24_26c7d2333b51
        edge_no_leak_d67f0.result_node = node_1c4e04e0_c37e_2eef_6de3_437f4b83142c
        edge_no_17cdb.result_node = node_49f721fc_2b60_1241_fefe_3fde197359ba
        edge__c5c61.result_node = node_d45d94b0_302e_442d_5069_267cc52167ee
        edge__045e5.result_node = node_data_leak_48217
        edge_leak_39160.result_node = node_de9eeec0_8116_f60f_6f73_2efe98bbe768
        edge_no_leak_7c43a.result_node = node_9c03659f_66f6_36f7_3ab7_d53ac2f7d970

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

    strategy = StrategyNew(city)
    tree = strategy.build_tree()
    tree.print_tree()