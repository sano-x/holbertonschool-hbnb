class User {
  id: string;
  name: string;
  email: string;
  passwordHash: string;
  role: 'guest' | 'host' | 'admin'; // Гость, Хост, Админ
  phone?: string;
  avatar?: string;
  verified: boolean; // Подтверждён ли email/телефон
  createdAt: Date;
  updatedAt: Date;

  // Методы
  becomeHost(): void; // Перевести в роль 'host'
  verifyAccount(): void; // Подтвердить email/телефон
  updateProfile(data: { name?: string; phone?: string }): void;
}