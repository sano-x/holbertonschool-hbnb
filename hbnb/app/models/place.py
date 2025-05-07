class Place {
  id: string;
  title: string;
  description: string;
  type: 'apartment' | 'house' | 'villa' | 'room'; // Тип жилья
  address: string;
  location: { lat: number; lng: number };
  pricePerNight: number;
  maxGuests: number;
  bedrooms: number;
  beds: number;
  amenities: Amenity[]; // Список удобств (Wi-Fi, бассейн и т. д.)
  images: string[]; // Фотографии жилья
  host: User; // Владелец
  isAvailable: boolean; // Доступно для бронирования
  createdAt: Date;
  updatedAt: Date;

  // Методы
  updateAvailability(status: boolean): void;
  addAmenity(amenity: Amenity): void;
  removeAmenity(amenityId: string): void;
}