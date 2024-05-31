import React, { useEffect, useRef } from 'react';

import { Loader } from "@googlemaps/js-api-loader"

// Replace 'YOUR_API_KEY' with your actual Google Maps API key
const API_KEY = process.env.REACT_APP_GOOGLE_MAPS_API_KEY || '';

interface MapComponentProps {
  additionalOptions?: any;
}


const MapComponent: React.FC<MapComponentProps> = ({ additionalOptions }) => {
  const mapRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const loader = new Loader({
      apiKey: API_KEY,
      version: "weekly",
      ...additionalOptions,
    });

    loader.load().then(async () => {
      const { Map } = await google.maps.importLibrary("maps") as google.maps.MapsLibrary;
      map = new Map(document.getElementById("map") as HTMLElement, {
        center: { lat: -34.397, lng: 150.644 },
        zoom: 8,
      });
    });
  }, [additionalOptions]);

  return <div ref={mapRef} style={{ height: '500px', width: '100%' }} />;
};

export default MapComponent;