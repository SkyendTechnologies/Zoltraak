// main.rs

mod logs;
mod blocks;
mod blockchain;
mod transactions;

use blockchain::Blockchain;
use transactions::transaction::Transaction;
use log::info;
use std::sync::Arc;
use tokio::sync::Mutex;

#[tokio::main]
async fn main() {
    logs::init(log::LevelFilter::Info).unwrap();

    // Создаем потокобезопасную обертку
    let blockchain = Arc::new(Mutex::new(Blockchain::new(2)));

    // Добавляем транзакции
    let transaction1 = Transaction::new(
        "Alice".to_string(),
        "Bob".to_string(),
        50,
        "signature_placeholder".to_string(),
        chrono::Utc::now().timestamp() as u64,
    );

    {
        let mut blockchain_guard = blockchain.lock().await;
        blockchain_guard.add_transaction(transaction1);
    //    blockchain_guard.add_transaction(transaction2);
    //     blockchain_guard.add_transaction(transaction3);
    }

    // Запуск асинхронного майнинга
    let blockchain_clone = Arc::clone(&blockchain);
    let mining_task = tokio::spawn(async move {
        let mut blockchain_guard = blockchain_clone.lock().await;
        blockchain_guard.mine_pending_transactions().await;
    });

    mining_task.await.unwrap();

    // Доступ к блокчейну после майнинга
    let blockchain_guard = blockchain.lock().await;
    info!("Содержимое блокчейна: {:#?}", blockchain_guard.chain);
}
