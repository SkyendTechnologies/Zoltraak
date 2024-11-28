use crate::blocks::block::Block;
use crate::transactions::transaction::Transaction;
use log::info;

pub struct Blockchain {
    pub chain: Vec<Block>,
    pub pending_transactions: Vec<Transaction>,
    pub difficulty: usize,
}

impl Blockchain {
    // Создание нового блокчейна с начальным генезис-блоком
    pub fn new(difficulty: usize) -> Self {
        let genesis_block = Block::new_genesis_block();
        Blockchain {
            chain: vec![genesis_block],
            pending_transactions: Vec::new(),
            difficulty,
        }
    }

    // Метод для добавления транзакции в список ожидающих
    pub fn add_transaction(&mut self, transaction: Transaction) {
        self.pending_transactions.push(transaction);
    }

    // Асинхронная функция для майнинга блока
    pub async fn mine_pending_transactions(&mut self) {
        info!("Запуск майнинга...");

        // Создаем новый блок, который будет содержать транзакции
        let mut new_block = Block {
            index: self.chain.len() as u64,
            timestamp: tokio::time::Instant::now().elapsed().as_secs(),
            transactions: self.pending_transactions.clone(),
            previous_hash: self.chain.last().unwrap().hash.clone(),
            hash: String::new(), // Начальный хеш будет вычислен в процессе майнинга
            nonce: 0,
        };

        // Майним блок (с использованием асинхронного метода)
        new_block.mine_block(self.difficulty).await;

        // После майнинга блок добавляется в цепочку, и транзакции очищаются
        self.chain.push(new_block);
        self.pending_transactions.clear();

        info!("Майнинг завершен.");
    }
}
