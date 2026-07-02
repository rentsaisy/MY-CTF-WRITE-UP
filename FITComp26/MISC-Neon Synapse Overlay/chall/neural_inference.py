import json
import sys
import os

def simulate_neural_activity(matrix_path):
    with open(matrix_path, 'r') as f:
        data = json.load(f)

    matrix = data['personality_matrix']
    potential_offset = data['entry_node']

    # [SNP v4.0.b] - SECURE NEURAL PROCESSOR
    neurotransmitter_stack = []
    synapse_buffer = []

    # Synchronization state - initialized from environment
    sync_key = os.getenv("PERSONALITY_SYNC", "")
    ion_alignment = sum(ord(c) for c in sync_key) % 256 if sync_key else 0

    print(f"[SNP] Ion Alignment: {hex(ion_alignment)}")

    while potential_offset < len(matrix):
        impulse = matrix[potential_offset]
        potential_offset += 1

        if impulse == 10:  # PULSE
            neurotransmitter_stack.append(matrix[potential_offset])
            potential_offset += 1
        elif impulse == 20:  # SYNAPSE_BOND
            b = neurotransmitter_stack.pop()
            a = neurotransmitter_stack.pop()
            neurotransmitter_stack.append(a + b)
        elif impulse == 30:  # ION_XOR
            b = neurotransmitter_stack.pop()
            a = neurotransmitter_stack.pop()
            neurotransmitter_stack.append(a ^ b)
        elif impulse == 40:  # ACTION_POTENTIAL
            addr = matrix[potential_offset]
            potential_offset += 1
            threshold = neurotransmitter_stack.pop()
            if threshold == 0:
                potential_offset = addr
        elif impulse == 50:  # VESICLE_OUT
            val = neurotransmitter_stack.pop()
            synapse_buffer.append(chr(val % 256))
        elif impulse == 60:  # APOPTOSIS
            print("[SNP] Neural activity finalized.")
            break
        elif impulse == 70:  # DENDRITE_RETRIEVAL
            addr = neurotransmitter_stack.pop()
            neurotransmitter_stack.append(matrix[addr])
        else:
            pass

    print("--- RECOVERED PERSONALITY FRAGMENT ---")
    print("".join(synapse_buffer))
    print("--------------------------------------")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python neural_inference.py <synapse_weights.json>")
    else:
        simulate_neural_activity(sys.argv[1])
