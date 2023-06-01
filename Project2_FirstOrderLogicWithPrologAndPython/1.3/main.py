from knowledge_base import KnowledgeBase
from fact import Fact

# Edit input knowledge, query and output path here
inp_file = 'knowledge_1.1.pl'
query_file = 'query_1.1.pl'
outp_file = 'answers.txt'

kb = KnowledgeBase()
with open(inp_file, 'r') as f_in:
   list_sentences = f_in.readlines()
   KnowledgeBase.declare(kb, list_sentences)

print('Done initialize knowledge base from {}.'.format(inp_file))

with open(query_file, 'r') as f_query:
   with open(outp_file, 'w') as f_out:
      for query_str in f_query.readlines():
         alpha = Fact.parse_fact(query_str)
         alpha_str = str(alpha) + '.'
         print(alpha_str)
         substs = set(kb.query(alpha))
         substs_str = ' ;\n'.join([str(subst) for subst in substs]) + '.\n'
         print(substs_str)
         f_out.write(alpha_str + '\n')
         f_out.write(substs_str + '\n')

print('Results of queries from {} are written to {}.'.format(query_file, outp_file))