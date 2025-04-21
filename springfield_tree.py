# Previously completed TerminalNode examples
from nodes import ChanceEdge, ChanceNode, DecisionEdge, DecisionNode, TerminalNode

# 1) Terminal nodes
terminal_892f5180 = TerminalNode(id="892f5180-47b6-0e81-8aed-4464a8e3c008", name="Terminal")
terminal_c5b874a6 = TerminalNode(id="c5b874a6-5b88-2f46-a4cb-98e70f7ee443", name="Terminal")

# 2) Data Leak? (–319,168 / 0)
data_leak1_yes = ChanceEdge("Leak", -319168, 0.5166666666666667)
data_leak1_no  = ChanceEdge("No Leak", 0, 0.4833333333333333)
data_leak1_node = ChanceNode("Data Leak?", [data_leak1_yes, data_leak1_no])

# 3) More terminal nodes
terminal_9e3c94db = TerminalNode(id="9e3c94db-a639-2da0-905a-ef8ef5443f76", name="Terminal")
terminal_4da370b8 = TerminalNode(id="4da370b8-e53b-0822-ee30-7f47838c51f5", name="Terminal")

# 4) Data Leak? (–3,691,680 / 0)
data_leak2_yes = ChanceEdge("Leak", -3691680, 0.5166666666666667)
data_leak2_no  = ChanceEdge("No Leak", 0, 0.4833333333333333)
data_leak2_node = ChanceNode("Data Leak?", [data_leak2_yes, data_leak2_no])

# 5) Key? (164,243,000 / –66,045,000)
key1_yes = ChanceEdge("Obtain Key", 164243000, 0.7966666666666666)
key1_no  = ChanceEdge("No key", -66045000, 0.20333333333333337)
key1_node = ChanceNode("Key?", [key1_yes, key1_no])

# 6) Pay Ransom (single choice)
pay_ransom1_edge = DecisionEdge("paid", -164243000)
pay_ransom1_node = DecisionNode("Pay Ransom", [pay_ransom1_edge])

# 7) Terminal node
terminal_0b9e74c9 = TerminalNode(id="0b9e74c9-e702-fecc-e9b7-7b5099fc2661", name="Terminal")

# 8) Attack? (Yes/No)
attack1_yes = ChanceEdge("Yes", 0, 0.03833333333333333)
attack1_no  = ChanceEdge("No", 0, 0.9616666666666667)
attack1_node = ChanceNode("Attack?", [attack1_yes, attack1_no])

# 9) Do Nothing (single choice)
do_nothing_edge = DecisionEdge("", 0)
do_nothing_node = DecisionNode("Do Nothing", [do_nothing_edge])

# 10–11) More terminals
terminal_dba2a79e = TerminalNode(id="dba2a79e-7241-4660-cbb4-a14f466e5713", name="Terminal")
terminal_c7cd1883 = TerminalNode(id="c7cd1883-d39b-4024-dfa1-9b2f7cfed392", name="Terminal")

# 12) Data Leak? (–319,168 / 0) again
data_leak3_yes = ChanceEdge("Leak", -319168, 0.5166666666666667)
data_leak3_no  = ChanceEdge("No Leak", 0, 0.4833333333333333)
data_leak3_node = ChanceNode("Data Leak?", [data_leak3_yes, data_leak3_no])

# 13–14) More terminals
terminal_4eef8a6a = TerminalNode(id="4eef8a6a-d256-c390-f39f-b15d737729d3", name="Terminal")
terminal_ff0e1b89 = TerminalNode(id="ff0e1b89-3e02-d449-2a8b-5b808c67d333", name="Terminal")

# 15) Data Leak? (–3,691,680 / 0) again
data_leak4_yes = ChanceEdge("Leak", -3691680, 0.5166666666666667)
data_leak4_no  = ChanceEdge("No Leak", 0, 0.4833333333333333)
data_leak4_node = ChanceNode("Data Leak?", [data_leak4_yes, data_leak4_no])

# 16) Key? (0 / –66,045,000)
key2_yes = ChanceEdge("Obtain Key", 0, 0.7966666666666666)
key2_no  = ChanceEdge("No key", -66045000, 0.20333333333333337)
key2_node = ChanceNode("Key?", [key2_yes, key2_no])

# 17–18) More terminals
terminal_3a016884 = TerminalNode(id="3a016884-7d74-c60e-e39b-1dcd89a93bf0", name="Terminal")
terminal_6bdc5172 = TerminalNode(id="6bdc5172-1b34-3e78-f115-8260853e35f6", name="Terminal")

# 19) Data Leak? (–319,168 / 0) yet again
data_leak5_yes = ChanceEdge("Leak", -319168, 0.5166666666666667)
data_leak5_no  = ChanceEdge("No Leak", 0, 0.4833333333333333)
data_leak5_node = ChanceNode("Data Leak?", [data_leak5_yes, data_leak5_no])

# 20) Pay Ransom (paid / don't pay)
pay_ransom2_yes = DecisionEdge("paid", -164243000)
pay_ransom2_no  = DecisionEdge("Don't pay", 0)
pay_ransom2_node = DecisionNode("Pay Ransom", [pay_ransom2_yes, pay_ransom2_no])

# 21) Terminal
terminal_08e2510b = TerminalNode(id="08e2510b-0401-63d8-899e-e96f0634f448", name="Terminal")

# 22) Attack? again
attack2_yes = ChanceEdge("Yes", 0, 0.03833333333333333)
attack2_no  = ChanceEdge("No", 0, 0.9616666666666667)
attack2_node = ChanceNode("Attack?", [attack2_yes, attack2_no])

# 23) No Backup (single choice)
no_backup_edge = DecisionEdge("", 0)
no_backup_node = DecisionNode("No Backup", [no_backup_edge])

# 24) Terminal
terminal_83a180b1 = TerminalNode(id="83a180b1-5660-749e-44fc-6b0b30243514", name="Terminal")

# 25) Another terminal
terminal_7aeb7fce = TerminalNode(id="7aeb7fce-96a0-5325-066d-9ce2ddb09242", name="Terminal")

# 26) Data Leak? (–319,168 / 0) yet again
data_leak6_yes = ChanceEdge("Leak", -319168, 0.5166666666666667)
data_leak6_no  = ChanceEdge("No Leak", 0, 0.4833333333333333)
data_leak6_node = ChanceNode("Data Leak?", [data_leak6_yes, data_leak6_no])

# 27–28) More terminals
terminal_73edb5a9 = TerminalNode(id="73edb5a9-7027-a877-bd1d-6352009d47c3", name="Terminal")
terminal_1eee9364 = TerminalNode(id="1eee9364-9819-f8b6-cb21-d90e1298867d", name="Terminal")

# 29) Data Leak? (–3,691,680 / 0) yet again
data_leak7_yes = ChanceEdge("Leak", -3691680, 0.5166666666666667)
data_leak7_no  = ChanceEdge("No Leak", 0, 0.4833333333333333)
data_leak7_node = ChanceNode("Data Leak?", [data_leak7_yes, data_leak7_no])

# 30) Key? (0 / –66,045,000) again
key3_yes = ChanceEdge("Obtain Key", 0, 0.7966666666666666)
key3_no  = ChanceEdge("No key", -66045000, 0.20333333333333337)
key3_node = ChanceNode("Key?", [key3_yes, key3_no])

# 31–32) More terminals
terminal_5300516e = TerminalNode(id="5300516e-cc7e-566c-3e71-956de1229c89", name="Terminal")
terminal_c2009aa5 = TerminalNode(id="c2009aa5-fcdf-b4f5-a95d-4ef3a1b05756", name="Terminal")

# 33) Data Leak? (–3,691,680 / 0) once more
data_leak8_yes = ChanceEdge("Leak", -3691680, 0.5166666666666667)
data_leak8_no  = ChanceEdge("No Leak", 0, 0.4833333333333333)
data_leak8_node = ChanceNode("Data Leak?", [data_leak8_yes, data_leak8_no])

# 34) Pay Ransom (third group)
pay_ransom3_yes = DecisionEdge("paid", -164243000)
pay_ransom3_no  = DecisionEdge("Don't pay", 0)
pay_ransom3_node = DecisionNode("Pay Ransom", [pay_ransom3_yes, pay_ransom3_no])

# 35–36) More terminals
terminal_f2141636 = TerminalNode(id="f2141636-b18c-1d09-5d24-26c7d2333b51", name="Terminal")
terminal_1c4e04e0 = TerminalNode(id="1c4e04e0-c37e-2eef-6de3-437f4b83142c", name="Terminal")

# 37) Data Leak? (–319,168 / 0) again
data_leak9_yes = ChanceEdge("Leak", -319168, 0.5166666666666667)
data_leak9_no  = ChanceEdge("No Leak", 0, 0.4833333333333333)
data_leak9_node = ChanceNode("Data Leak?", [data_leak9_yes, data_leak9_no])

# 38) Backup Good? (Failed / —)
backup_good_failed = ChanceEdge("Failed", 0, 0.7316666666666667)
backup_good_no     = ChanceEdge("", 0, 0.2683333333333333)
backup_good_node   = ChanceNode("Backup Good? ", [backup_good_failed, backup_good_no])

# 39) Terminal
terminal_49f721fc = TerminalNode(id="49f721fc-2b60-1241-fefe-3fde197359ba", name="Terminal")

# 40) Attack? (third one)
attack3_yes = ChanceEdge("Yes", 0, 0.03833333333333333)
attack3_no  = ChanceEdge("No", 0, 0.9616666666666667)
attack3_node = ChanceNode("Attack?", [attack3_yes, attack3_no])

# 41) Backup (single choice)
backup_edge = DecisionEdge("", 0)
backup_node = DecisionNode("Backup", [backup_edge])

# 42) In‑House IT Security Department
in_house_it_edge1 = DecisionEdge("", 0)
in_house_it_edge2 = DecisionEdge("", 0)
in_house_it_node  = DecisionNode(
    "In-House IT Security Department \n(With End User Training, Insurance)\n",
    [in_house_it_edge1, in_house_it_edge2]
)

# 43–44) More terminals
terminal_de9eeec0 = TerminalNode(id="de9eeec0-8116-f60f-6f73-2efe98bbe768", name="Terminal")
terminal_9c03659f = TerminalNode(id="9c03659f-66f6-36f7-3ab7-d53ac2f7d970", name="Terminal")

# 45) Data Leak? (–319,168 / 0.1)
data_leak10_yes = ChanceEdge("Leak", -319168, 0.1)
data_leak10_no  = ChanceEdge("No Leak", 0, 0.9)
data_leak10_node = ChanceNode("Data Leak?", [data_leak10_yes, data_leak10_no])

# 46) External IT Security (single choice)
external_it_edge = DecisionEdge("", 0)
external_it_node = DecisionNode("External IT Security\n(Insurance Included)", [external_it_edge])

# 47) Strategy Packages (3 choices)
strategy_edge1 = DecisionEdge("", 0)
strategy_edge2 = DecisionEdge("", -1814964)
strategy_edge3 = DecisionEdge("", -600000)
strategy_node  = DecisionNode("Strategy Packages", [strategy_edge1, strategy_edge2, strategy_edge3])

# ────────────────────────────────
# 1) Top‑level Strategy Packages
# ────────────────────────────────
strategy_edge1.result_node = do_nothing_node
strategy_edge2.result_node = in_house_it_node
strategy_edge3.result_node = external_it_node

# ────────────────────────────────
# 2) “Do Nothing” branch (strategy_edge1)
# ────────────────────────────────
do_nothing_edge.result_node       = data_leak1_node

data_leak1_yes.result_node        = data_leak2_node
data_leak1_no.result_node         = terminal_9e3c94db

data_leak2_yes.result_node        = key1_node
data_leak2_no.result_node         = terminal_4da370b8

key1_yes.result_node              = pay_ransom1_node
key1_no.result_node               = terminal_0b9e74c9

pay_ransom1_edge.result_node      = attack1_node

attack1_yes.result_node           = do_nothing_node
attack1_no.result_node            = terminal_dba2a79e

# that “Do Nothing” (second) goes to the final terminal
do_nothing_edge.result_node       = terminal_c7cd1883

# ────────────────────────────────
# 3) In‑House IT branch (strategy_edge2)
# ────────────────────────────────
in_house_it_edge1.result_node     = no_backup_node
in_house_it_edge2.result_node     = backup_node

# 3a) No‑Backup subtree
no_backup_edge.result_node        = attack2_node

attack2_yes.result_node           = pay_ransom2_node
attack2_no.result_node            = terminal_08e2510b

# both “paid” and “don't pay” feed the same leak check
pay_ransom2_yes.result_node       = data_leak5_node
pay_ransom2_no.result_node        = data_leak5_node

data_leak5_yes.result_node        = terminal_73edb5a9
data_leak5_no.result_node         = terminal_1eee9364

# 3b) Backup‑available subtree
backup_edge.result_node           = backup_good_node

backup_good_failed.result_node    = pay_ransom3_node
backup_good_no.result_node        = data_leak9_node

pay_ransom3_yes.result_node       = data_leak8_node
pay_ransom3_no.result_node        = data_leak8_node

data_leak8_yes.result_node        = terminal_5300516e
data_leak8_no.result_node         = terminal_c2009aa5

data_leak9_yes.result_node        = terminal_f2141636
data_leak9_no.result_node         = terminal_1c4e04e0

# ────────────────────────────────
# 4) External IT branch (strategy_edge3)
# ────────────────────────────────
external_it_edge.result_node      = data_leak10_node

data_leak10_yes.result_node       = terminal_de9eeec0
data_leak10_no.result_node        = terminal_9c03659f

strategy_node.print_tree()