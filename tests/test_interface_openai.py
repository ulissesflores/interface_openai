import unittest
import os
import logging
from app.interfaces.interface_openai import * 

# Configura o logging
log_file_path = os.path.join(os.path.dirname(__file__), '..', 'logs', 'test_logs.log')
logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

class TestInterfaceOpenAI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_file_path = os.path.join(os.path.dirname(__file__), 'oracao.pdf')
        assert os.path.exists(cls.test_file_path), "Arquivo de teste 'oracao.pdf' não existe no diretório esperado."
        logging.info("Configuração da classe de teste iniciada")

    def setUp(self):
        file_result = upload_file_to_openai(self.test_file_path)
        self.file_id = file_result.id if file_result else None
        logging.info("Setup antes de cada teste")

    def tearDown(self):
        logging.info("TearDown após cada teste")

    def test_upload_file(self):
        logging.info("Iniciando teste: test_upload_file")
        try:
            result = upload_file_to_openai(self.test_file_path)
            self.assertIsNotNone(result, "O resultado do upload é None, indicando falha no upload.")
            self.assertTrue(hasattr(result, 'id'), "O objeto de arquivo retornado não contém um atributo 'id'.")
            logging.info("Sucesso: test_upload_file")
        except AssertionError as e:
            logging.error(f"Falha: test_upload_file - {e}")
            raise

    def test_create_assistant_without_file(self):
        logging.info("Iniciando teste: test_create_assistant_without_file")
        try:
            assistant_result = create_assistant()
            self.assertIsNotNone(assistant_result, "Falha na criação do assistente sem arquivo.")
            self.assertTrue(hasattr(assistant_result, 'id'), "O assistente criado não possui um 'id'.")
            logging.info("Sucesso: test_create_assistant_without_file")
        except AssertionError as e:
            logging.error(f"Falha: test_create_assistant_without_file - {e}")
            raise

    def test_create_assistant_with_file(self):
        logging.info("Iniciando teste: test_create_assistant_with_file")
        if not self.file_id:
            logging.warning("Falha no upload do arquivo; teste de criação do assistente com arquivo pulado.")
            self.skipTest("Falha no upload do arquivo; teste de criação do assistente com arquivo pulado.")
        try:
            assistant_result = create_assistant(file_id=self.file_id)
            self.assertIsNotNone(assistant_result, "Falha na criação do assistente com arquivo.")
            self.assertTrue(hasattr(assistant_result, 'id'), "O assistente criado com arquivo não possui um 'id'.")
            logging.info("Sucesso: test_create_assistant_with_file")
        except AssertionError as e:
            logging.error(f"Falha: test_create_assistant_with_file - {e}")
            raise
    
    def test_retrieve_assistant(self):
        logging.info("Iniciando teste: test_retrieve_assistant")
        assistant_id = "algum_id_existente"  # Substitua isso pelo ID de um assistente existente para o teste
        try:
            assistant = retrieve_assistant(assistant_id)
            self.assertIsNotNone(assistant, "Falha na recuperação do assistente.")
            self.assertEqual(assistant.id, assistant_id, "O ID do assistente recuperado não corresponde ao esperado.")
            logging.info("Sucesso: test_retrieve_assistant")
        except AssertionError as e:
            logging.error(f"Falha: test_retrieve_assistant - {e}")
            raise
    
    # Teste para create_thread
    def test_create_thread(self):
        logging.info("Iniciando teste: test_create_thread")
        try:
            thread_result = create_thread()
            self.assertIsNotNone(thread_result, "Falha na criação do thread.")
            self.assertTrue(hasattr(thread_result, 'id'), "O thread criado não possui um 'id'.")
            logging.info("Sucesso: test_create_thread")
        except AssertionError as e:
            logging.error(f"Falha: test_create_thread - {e}")
            raise

    # Teste para retrieve_thread
    def test_retrieve_thread(self):
        logging.info("Iniciando teste: test_retrieve_thread")
        thread_id = "algum_id_de_thread_existente"  # Substitua pelo ID de um thread existente para teste
        try:
            thread = retrieve_thread(thread_id)
            self.assertIsNotNone(thread, "Falha na recuperação do thread.")
            self.assertEqual(thread.id, thread_id, "O ID do thread recuperado não corresponde ao esperado.")
            logging.info("Sucesso: test_retrieve_thread")
        except AssertionError as e:
            logging.error(f"Falha: test_retrieve_thread - {e}")
            raise

    # Teste para generate_response
    def test_generate_response(self):
        logging.info("Iniciando teste: test_generate_response")
        question_prompt = "Alguma pergunta relevante"  # Insira um prompt de pergunta relevante para o teste
        try:
            response = generate_response(question_prompt)
            self.assertIsNotNone(response, "Falha na geração da resposta.")
            self.assertIsInstance(response, str, "A resposta gerada não é uma string.")
            logging.info("Sucesso: test_generate_response")
        except AssertionError as e:
            logging.error(f"Falha: test_generate_response - {e}")
            raise

if __name__ == '__main__':
    unittest.main()
