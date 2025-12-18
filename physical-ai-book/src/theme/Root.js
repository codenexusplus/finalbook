import React, { createContext, useState, useEffect, useCallback } from 'react';

// 1. Create the context
export const SessionContext = createContext({
  user: null,
  isAuthenticated: false,
  isLoading: true,
  refetch: () => {},
});

// 2. Create the provider component
function SessionProvider({ children }) {
  const [user, setUser] = useState(null);
  const [isLoading, setIsLoading] = useState(true);

  const fetchUser = useCallback(async () => {
    setIsLoading(true);
    try {
      const response = await fetch('/api/users/me'); // Assuming backend is proxied
      if (response.ok) {
        const userData = await response.json();
        setUser(userData);
      } else {
        setUser(null);
      }
    } catch (error) {
      console.error("Failed to fetch user session", error);
      setUser(null);
    } finally {
      setIsLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchUser();
  }, [fetchUser]);

  const value = {
    user,
    isAuthenticated: !!user,
    isLoading,
    refetch: fetchUser,
  };

  return (
    <SessionContext.Provider value={value}>
      {children}
    </SessionContext.Provider>
  );
}

// 3. Create the Root wrapper component for Docusaurus
export default function Root({ children }) {
  return (
    <SessionProvider>
      {children}
    </SessionProvider>
  );
}
