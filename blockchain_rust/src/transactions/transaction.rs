use chrono::{Utc, DateTime};
use serde::{Serialize, Deserialize};
use log::info;

/// Структура транзакции, содержащая информацию о передаче средств от отправителя к получателю.
/// `sender` — адрес отправителя, `receiver` — адрес получателя, `amount` — количество средств,
/// `signature` — цифровая подпись для подтверждения права на перевод.

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Transaction {
    pub sender: String,
    pub receiver: String,
    pub amount: u64,
    pub signature: String,
    pub timestamp: u64,
}

impl Transaction {
    pub fn new(
        sender: String,
        receiver: String,
        amount: u64,
        signature: String,
        timestamp: u64,
    ) -> Self
    {
        info!("Новая транзакция создана.");
        Transaction {
            sender,
            receiver,
            amount,
            signature,
            timestamp: Utc::now().timestamp() as u64,
        }
    }

    /// Возвращает строковое представление транзакции
    pub fn to_string(&self) -> String {
        format!("{} -> {}: {}", self.sender, self.receiver, self.amount)
    }

    /// Возвращает количество средств в транзакции
    pub fn get_amount(&self) -> u64 {
        self.amount
    }

    /// Возвращает адрес отправителя транзакции
    pub fn get_sender(&self) -> String {
        self.sender.clone()
    }

    /// Возвращает адрес получателя транзакции
    pub fn get_receiver(&self) -> String {
        self.receiver.clone()
    }

    /// Возвращает цифровую подпись транзакции
    pub fn get_signature(&self) -> String {
        self.signature.clone()
    }

    /// Возвращает время создания транзакции
    pub fn get_timestamp(&self) -> DateTime<Utc> {
        DateTime::from_utc(chrono::NaiveDateTime::from_timestamp(self.timestamp as i64, 0), Utc)
    }

}
