class Review {
  id: string;
  place: Place; // О каком жилье отзыв
  author: User; // Кто оставил
  rating: number; // 1-5 звёзд
  comment: string;
  createdAt: Date;

  // Методы
  updateRating(newRating: number): void;
  editComment(newText: string): void;
}