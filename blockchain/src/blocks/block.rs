use serde::{Serialize, Deserialize};
use sha2::{Sha256, Digest};
use log::info;
use tokio::time::{sleep, Duration};
use chrono::Utc;
use crate::transactions::transaction::Transaction;

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Block {
    pub index: u64,
    pub timestamp: u64,
    pub transactions: Vec<Transaction>,
    pub previous_hash: String,
    pub hash: String,
    pub nonce: u64,
}

impl Block {
    /// Создание генезис-блока
    pub fn new_genesis_block() -> Block {
        let mut genesis_block = Block {
            index: 0,
            timestamp: Utc::now().timestamp() as u64,
            transactions: Vec::new(),
            previous_hash: String::from("0"),
            hash: String::new(),
            nonce: 0,
        };
        genesis_block.hash = genesis_block.calculate_hash();
        info!("Генезис-блок создан с хешем: {}", genesis_block.hash);
        genesis_block
    }

    /// Вычисление хеша блока
    pub fn calculate_hash(&self) -> String {
        let block_data = format!(
            "{}{}{:?}{}{}",
            self.index, self.timestamp, self.transactions, self.previous_hash, self.nonce
        );
        let mut hasher = Sha256::new();
        hasher.update(block_data);
        format!("{:x}", hasher.finalize())
    }

    /// Асинхронный майнинг блока
    pub async fn mine_block(&mut self, difficulty: usize) {
        info!("Начинается майнинг блока с индексом {}...", self.index);
        let target = "0".repeat(difficulty);

        // Убедитесь, что хеш имеет начальное значение
        if self.hash.is_empty() {
            self.hash = self.calculate_hash();
        }

        // Асинхронно ищем подходящий хеш, увеличивая nonce
        while &self.hash[..difficulty.min(self.hash.len())] != target {
            self.nonce += 1;
            self.hash = self.calculate_hash();

            // Имитация задержки майнинга
            sleep(Duration::from_millis(10)).await;
        }

        info!("Блок с индексом {} успешно замайнен: {}", self.index, self.hash);
    }
}