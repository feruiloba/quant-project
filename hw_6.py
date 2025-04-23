from nodes import ChanceEdge, ChanceNode, TerminalNode

edge_good_2b8a7 = ChanceEdge(name='good_e0e08', payoff=0, probability=0.75, id='good_23552')

node_c0d178ae_c5d7_76f0_8c15_30b2cb439806 = TerminalNode(name='_5e021', id='c0d178ae-c5d7-76f0-8c15-30b2cb439806')

node_861d64bc_fa42_d039_a398_12c2ab0a7eee = TerminalNode(name='_47dc4', id='861d64bc-fa42-d039-a398-12c2ab0a7eee')

edge_bad_ccfa3 = ChanceEdge(name='bad_a26d8', payoff=0, probability=0.25, id='bad_0c88d')

node_5f6ec0ca_4384_0cbc_90c7_ef20d99ea0ae = TerminalNode(name='_fce99', id='5f6ec0ca-4384-0cbc-90c7-ef20d99ea0ae')
prob_virus = 0.48
edge__4f741 = ChanceEdge(name='_ab103', payoff=-5000, probability=(1-prob_virus), id='_8b924')
edge_not_present_cb663 = ChanceEdge(name='not_present_15d78', payoff=10000, probability=(1-prob_virus), id='not_present_b459d')
edge_present_6b313 = ChanceEdge(name='present_74607', payoff=-7000, probability=prob_virus, id='present_ac8f2')
edge_present_ce173 = ChanceEdge(name='present_56c86', payoff=-7000, probability=prob_virus, id='present_5d808')
node_norovirus_522ea = ChanceNode(name='norovirus_055fb', id='norovirus_522ea', edges=[edge_not_present_cb663, edge_present_6b313])
node_01b0231e_7c13_eca0_ccc4_d52a70aac09c = TerminalNode(name='_4e4a6', id='01b0231e-7c13-eca0-ccc4-d52a70aac09c')
node_norovirus_a1f4f = ChanceNode(name='norovirus_8b980', id='norovirus_a1f4f', edges=[edge__4f741, edge_present_ce173])
node_weather_c486f = ChanceNode(name='weather_f401d', id='weather_c486f', edges=[edge_good_2b8a7, edge_bad_ccfa3])
edge_good_2b8a7.result_node = node_norovirus_522ea
edge_not_present_cb663.result_node = node_c0d178ae_c5d7_76f0_8c15_30b2cb439806
edge_present_6b313.result_node = node_861d64bc_fa42_d039_a398_12c2ab0a7eee
edge_bad_ccfa3.result_node = node_norovirus_a1f4f
edge__4f741.result_node = node_5f6ec0ca_4384_0cbc_90c7_ef20d99ea0ae
edge_present_ce173.result_node = node_01b0231e_7c13_eca0_ccc4_d52a70aac09c

node_weather_c486f.print_tree()