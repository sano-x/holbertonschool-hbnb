class Amenity {
  id: string;
  name: string; // "Wi-Fi", "Бассейн", "Кухня"
  icon: string; // Иконка (FontAwesome/Emoji)
  category: 'basic' | 'safety' | 'luxury'; // Категория удобства
}